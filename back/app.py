from datetime import date, timedelta
from flask import Flask, jsonify, request
import requests
from flask_cors import CORS
from pymongo import MongoClient
import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer

from question_generator import question_generator
from threading import Thread
from konlpy.tag import Okt
from bson.objectid import ObjectId
from collections import Counter
import random



file_path = "category.json"

app = Flask(__name__)
CORS(app)

# cursor.execute("SELECT * from User")
# data = cursor.fetchone()
# print(data)

mongo_connect = "mongodb+srv://admin:1234@cluster0.zyylgba.mongodb.net/brain?retryWrites=true&w=majority"
client = MongoClient(mongo_connect)
mongodb = client.brain


# 카테고리 별 뉴스 보기
@app.route("/news/category", methods=['POST'])
def news():
    body = request.json
    data = send_category_request(body)
    return jsonify(data), 200

def send_category_request(body):
    data = {
      "access_key": "9f7da60c-c993-459a-88c7-9a4230797087",
      "argument": {
        "query": "",
        "published_at": {
          "from": body['from'],
          "until": body['until']
        },
        "provider": [],
        "category": body['category'],
        "sort": {"date": "desc"},
        "hilight": 200,
        "return_from": (body['page']-1)*5,
        "return_size": 5,
        "fields": [
          "byline",
          "category",
          # "category_incident",
          # "provider_news_id"
        ]
      }
    }
    response = requests.post('https://tools.kinds.or.kr/search/news', json=data)
    data = response.json()
    return data


# 뉴스 상세보기
@app.route("/detail", methods=['Post'])
def detail():
    body = request.json
    print(body)
    news_id = body.get("news_id")
    print(11111111111111111111111)
    print(news_id)
    data = {
        "access_key": "9f7da60c-c993-459a-88c7-9a4230797087",
        "argument": {
            "news_ids": [
                news_id
            ],
            "fields": [
                "content",
                "byline",
                "category",
                # "category_incident",
                "images",
                # "provider_subject",
                # "provider_news_id",
                # "publisher_code"
            ]
        }
    }

    response = requests.post('https://tools.kinds.or.kr/search/news', json=data)
    data = response.json()
    content = data["return_object"]["documents"][0]["content"]

    # 키워드 추출
    print(content)
    keywords = extract_keywords(content)
    print("-------------------------")
    print(keywords)

    return jsonify({
        "content": content,
        "keywords": keywords
    }), 200



# 본문에서 키워드 추출
def extract_keywords(content):
    # 텍스트 전처리 (예: 특수 문자 제거, 소문자 변환)
    content = preprocess_text(content)

    # TF-IDF 벡터화
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([content])

    # 단어와 해당 단어의 TF-IDF 값을 추출
    feature_names = vectorizer.get_feature_names_out()

    # 상위 N개의 키워드 선택
    top_n = 5
    top_indices = tfidf_matrix.toarray()[0].argsort()[-top_n:][::-1]
    keywords = [feature_names[i] for i in top_indices]

    return keywords


# 텍스트 전처리 함수 예시 (필요에 따라 수정)
def preprocess_text(text):
    # 소문자 변환
    text = text.lower()
    # 특수 문자 제거
    text = re.sub('[^a-zA-Z0-9ㄱ-ㅣ가-힣]', ' ', text)
    # 공백 제거
    text = text.strip()

    return text


# 유저가 본 뉴스의 카테고리와 news_id 저장을 하면서 그 뉴스 보여줘야함
@app.route("/category/save", methods=['POST'])
def show_news_and_category_save():
    body = request.json
    news_id = body.get('news_id', None)
    category = body.get('category', None)
    user_id = "dded"
    category_cnt(user_id, news_id, category)
    Thread(target=quiz_create, args=(user_id, news_id)).start()

    data = {
        "access_key": "9f7da60c-c993-459a-88c7-9a4230797087",
        "argument": {
            "news_ids": [
                news_id
            ],
            "fields": [
                "content",
                "category"
            ]
        }
    }

    response = requests.post('https://tools.kinds.or.kr/search/news', json=data)
    data = response.json()
    content = data["return_object"]["documents"][0]["content"]

    keywords = extract_keywords(content)
    # print(keywords)
    mongodb.users.update_one({"user_id": user_id},
                                  {"$push": {"keywords": {"$each": keywords}}}, upsert=True)

    return jsonify(data), 200



# 카테고리 저장 및 news_id 저장
def category_cnt(user_id, news_id, category_list):
    with open(file_path, "r", encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    categories = json_data.get('category', [])
    for category in categories:
        if category in category_list:
            mongodb.categories.update_one({'user_id': user_id}, {'$inc': {f'category.{category}': 1}}, upsert=True)



# 유저의 카테고리에 있는거 키워드의 중요한 부분 5개
@app.route("/recommend/my", methods=['POST'])
def recommend_news():
    body = request.json
    user_id = "dded"
    # user_id = body.get("dded", None)
    today = date.today().strftime("%Y-%m-%d")
    tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    # 몽고디비에서 해당 user_id의 문서를 조회하여 keyword 배열 가져오기
    user_collection = mongodb.users
    user_document = user_collection.find_one({"user_id": user_id})
    keywords = user_document.get("keywords",[])
    print("keywordsdddddddddddddddddddddddddddd")
    print(keywords)

    # keywords 배열의 중요한 부분 5개 선택
    important_keywords = select_important_keywords(keywords)
    print("important_keywordssssssssssssssssssssssssssssssss")
    print(important_keywords)
    query = "" if not important_keywords else " OR ".join(important_keywords)

    data = {
        "access_key": "9f7da60c-c993-459a-88c7-9a4230797087",
        "argument": {
            "query": query,
            "published_at": {
                "from": today,
                "until": tomorrow
            },
            "byline": "",
            "sort": [{"_score": "desc"}, {
                "date": "desc"}],
            "hilight": 500,
            "return_from": 0,
            "return_size": 20,
            "fields": [
                "content",
                "category",
            ]
        }
    }

    response = requests.post('https://tools.kinds.or.kr/search/news', json=data)
    data = response.json()

    return jsonify(data), 200


# 중요한 키워드 선택 함수
def select_important_keywords(keywords):
    # 첨에 아무것도 없을면 그냥 false 리턴
    if not keywords:
        return False
    # 키워드 배열을 하나의 텍스트로 변환
    user_keywords_text = ' '.join(keywords)

    # TF-IDF 벡터화
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([user_keywords_text])

    # 단어와 해당 단어의 TF-IDF 값을 추출
    feature_names = vectorizer.get_feature_names_out()

    # 상위 5개의 키워드 선택
    top_n = 5
    top_indices = tfidf_matrix.toarray()[0].argsort()[-top_n:][::-1]
    important_keywords = [feature_names[i] for i in top_indices]

    return important_keywords


# 퀴즈 생성 함수
def quiz_create(user_id, news_id):
    quiz = mongodb.quiz.find_one({'news_id': news_id})
    if not quiz:
        # 뉴스 디테일 불러오기
        data = send_detail_request(news_id)
       
        # 키워드 추출
        keywords = get_keywords(data.get("return_object").get("documents")[0].get("content"), 10)
       
        # 단답형 문제 생성
        answer, question = question_generator(data.get("return_object").get("documents")[0].get("content"))
        
        # 단어 목록 퀴즈 생성
        create_word_list_quiz(user_id, news_id, keywords)
        
        # 4지선다 이야기 회상형 퀴즈 생성
        create_choice_quiz(user_id, news_id, keywords, answer, question)


# 단어 목록 퀴즈 생성 함수
def create_word_list_quiz(user_id, news_id, keywords):
    doc = {'user_id': user_id, "quiz_question": "해당 단어들을 기억하세요", "example": keywords, "answer":0, "quiz_type": 0, "news_id": news_id, "number":0}
    mongodb.quiz.insert_one(doc)



# 선택형 퀴즈 생성 함수
def create_choice_quiz(user_id, news_id, keywords, answer, question):
    # 보기 생성
    other_words = [word for word in keywords if word != answer]

    # 보기 선택
    choices = random.sample(other_words, 3)

    # 보기 + 정답
    all_choices = choices + [answer]
    random.shuffle(all_choices)
    
    # 셔플
    example = {str(i + 1): choice for i, choice in enumerate(all_choices)}
    answer_number = [key for key, value in example.items() if value == answer][0]

    docdoc = {'user_id': user_id, "quiz_question": question, "example": example, "answer": answer_number, "quiz_type": 1, "news_id": news_id}
    mongodb.quiz.insert_one(docdoc)



# 키워드 뽑기
def get_keywords(content, n):

    # 형태소 분석기
    okt = Okt()

    # 문장에서 명사 추출
    nouns = okt.nouns(content)

    # 빈도 계산
    count = Counter(nouns)

    # 빈도가 높은 순으로 n개
    top_nouns = [noun for noun, freq in count.most_common(n)]

    return top_nouns



# 4지선다 퀴즈 정답 제출
@app.route("/choice/answer", methods=['POST'])
def choice_answer():
    body = request.json
    user_id = body.get("user_id")
    quiz_id = body.get("quiz_id")
    answer = body.get("answer")
    choice_quiz_answer(user_id, quiz_id, answer)

    return jsonify({"status": 200}), 200



# 4지선다 퀴즈 정답 제출 및 결과 저장
def choice_quiz_answer(user_id, quiz_id, answer):
    quiz = mongodb.quiz.find_one({"_id": ObjectId(quiz_id), "quiz_type": 1})
    if quiz.get("answer") == answer:
        mongodb.quiz_result.insert_one({"quiz_id": quiz_id, "user_id": user_id, "correct": 1, "answer":quiz.get("answer"), "quiz_type": 1, "my_answer":answer})
    else:
        mongodb.quiz_result.insert_one({"quiz_id": quiz_id, "user_id": user_id, "correct": 0, "answer":quiz.get("answer"), "quiz_type": 1, "my_answer":answer})



# 단어 목록 퀴즈 정답 제출
@app.route("/list/answer", methods=['POST'])
def list_answer():
    body = request.json
    user_id = body.get("user_id")
    quiz_id = body.get("quiz_id")
    answer = body.get("answer")
    list_quiz_answer(user_id, quiz_id, answer)

    return jsonify({"status": 200}), 200


# 단어 목록 퀴즈 정답 제출 및 결과 저장
def list_quiz_answer(user_id, quiz_id, answer):
    quiz = mongodb.quiz.find_one({"_id": ObjectId(quiz_id), "quiz_type": 0})
    example = quiz.get("example")
    correct = 0
    result = {}
    for ex in quiz.get("example"):
        if ex in answer:
            result[ex] = 1
            correct += 1
        else:
            result[ex] = 0

    mongodb.quiz_result.insert_one({"quiz_id": quiz_id, "user_id": user_id, "correct": correct, "number": quiz.get("number")+1, "quiz_type": 0, "result":result})
    random.shuffle(example)
    mongodb.quiz.update_one({"_id": ObjectId(quiz_id), "quiz_type": 0}, {"$set": {"number": quiz.get("number")+1, "example": example}})

    # if quiz.get("number")+1 == 3:



# 뉴스 디테일 불러와서 사용
def send_detail_request(news_id):
    data = {
      "access_key": "9f7da60c-c993-459a-88c7-9a4230797087",
      "argument": {
        "news_ids": [
          news_id
        ],
        "fields": [
          "content",
          "byline",
          "category",
          # "category_incident",
          # "images",
          # "provider_subject",
          # "provider_news_id",
          # "publisher_code"
        ]
      }
    }
    response = requests.post('https://tools.kinds.or.kr/search/news', json=data)
    data = response.json()
    return data





# 나의 퀴즈 보기
@app.route("/user/myQuiz", methods=['POST'])
def my_quiz():
    user_id = request.json.get('user_id')
    user = list(mongodb.quiz.find({'user_id': user_id}))

    print(user)
    quizList = json.dumps(user, default=str, ensure_ascii=False)
    return quizList


# 퀴즈 다시 풀기
@app.route("/quiz/retry/answer", methods=['POST'])
def retry_answer():
    quiz_id = request.json.get('quiz_id')
    my_answer = request.json.get('answer')
    quiz = mongodb.quiz.find_one({'_id': ObjectId(quiz_id)})
    user_id = quiz.get('user_id')
    quiz_type = quiz.get('quiz_type')

    if quiz_type == 0:
        quiz_length = len(list(mongodb.quiz_result.find({'quiz_id':quiz_id})))
        example = quiz.get('example')
        correct = 0
        result = {}
        for i in example:
            result[i] = 0
            if i in my_answer:
                correct += 1
                result[i] = 1
        data = {
            'quiz_id' : quiz_id,
            'user_id' : user_id,
            'correct' : correct,
            'number' : quiz_length + 1,
            'quiz_type' : 0,
            'result' : result
        }
        mongodb.quiz_result.insert_one(data)
    elif quiz_type == 1 :
        answer = quiz.get('answer')
        if my_answer == answer:
            mongodb.quiz_result.update_one({'quiz_id': quiz_id},{'$set':{'correct': 1,'my_answer': my_answer}})
    return jsonify({"status": 200}), 200






# 서버 올릴 때 설정
# if __name__=='__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)