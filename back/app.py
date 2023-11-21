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
            "return_from": (body['page'] - 1) * 5,
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

    news_id = body.get("news_id")

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
    keywords = extract_keywords(content)

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
    user_id = body.get('user_id', None)
    category_cnt(user_id, news_id, category)

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
            # 먼저 news_id를 추가
            mongodb.categories.update_one(
                {'user_id': user_id},
                {'$addToSet': {'current_news_id_lst': news_id}},
                upsert=True
            )

            # 그런 다음 배열의 크기를 조절
            mongodb.categories.update_one(
                {'user_id': user_id},
                {'$push': {'current_news_id_lst': {'$each': [], '$slice': -3}}, '$inc': {f'category.{category}': 1}},
                upsert=True
            )


# 유저의 카테고리에 있는거 키워드의 중요한 부분 5개
@app.route("/recommend/my", methods=['POST'])
def recommend_news():
    body = request.json
    user_id = body.get("user_id", None)
    today = date.today().strftime("%Y-%m-%d")
    tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    # 몽고디비에서 해당 user_id의 문서를 조회하여 keyword 배열 가져오기
    user_collection = mongodb.users
    user_document = user_collection.find_one({"user_id": user_id})
    keywords = user_document.get("keywords", [])

    # keywords 배열의 중요한 부분 5개 선택
    important_keywords = select_important_keywords(keywords)
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



# 단어 목록 퀴즈 생성 함수
def create_word_list_quiz(user_id, keywords, date):
    doc = {'user_id': user_id, "quiz_question": "해당 단어들을 기억하세요", "example": keywords, "answer": 0, "quiz_type": "j4",
           "number": 0, "date": date}
    mongodb.quiz.insert_one(doc)

# 단어 목록 퀴즈 j6 생성 함수
def create_word_list_quiz_z6(user_id, keywords, date):
    doc = {'user_id': user_id, "quiz_question": "해당 단어들을 기억하세요", "example": keywords, "answer":0, "quiz_type": "j6",  "number":0, "date":date}
    mongodb.quiz.insert_one(doc)



# 단어 목록 퀴즈 20 생성 함수
def create_word_list2_quiz(user_id, keywords, date):
    # 단어 사전 읽기/키워드에 있는 단어 제외
    with open('dict.txt', 'r', encoding='utf-8') as f:
        non_keywords = [line.strip() for line in f if line.strip() not in keywords]

    # 10개 선택
    random_words = random.sample(non_keywords, 10)

    # 보기 리스트
    new_list = list(random_words)

    # 보기 리스트 + 정답
    new_list.extend(keywords)

    # 셔플
    random.shuffle(new_list)

    doc = {'user_id': user_id, "quiz_question": "어떤 단어들을 보셨었나요", "example": new_list, "answer": keywords,
           "quiz_type": "j7", "number": 0, "date": date}
    mongodb.quiz.insert_one(doc)


# 선택형 퀴즈 생성 함수
def create_choice_quiz(user_id, content, answer, question, date):
    keywords = get_keywords(content, 10)

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

    return {"quiz_question": question, "example": example, "answer": answer_number}


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
@app.route("/choice/answer/j3", methods=['POST'])
def choice_answer():
    body = request.json
    user_id = body.get("user_id")
    quiz_id = body.get("quiz_id")
    answer = body.get("answer")
    choice_quiz_answer(user_id, quiz_id, answer)

    return jsonify({"status": 200}), 200


# 4지선다 퀴즈 정답 제출 및 결과 저장
def choice_quiz_answer(user_id, quiz_id, answer):
    quiz = mongodb.quiz.find_one({"_id": ObjectId(quiz_id), "quiz_type": "j3"})
    correct = 0

    for i in range(1, 4):
        if quiz.get("result").get(str(i)).get("answer") == answer.get(str(i)):
            correct += 1

    mongodb.quiz_result.insert_one({"quiz_id": quiz_id, "user_id": user_id, "correct": correct, "quiz_type": "j3", "date" : quiz.get("date")})


# 단어 목록 퀴즈 정답 제출
@app.route("/list/answer", methods=['POST'])
def list_answer():
    body = request.json
    user_id = body.get("user_id")
    quiz_id = body.get("quiz_id")
    answer = body.get("answer")

    if list_quiz_answer(user_id, quiz_id, answer):
        quiz = mongodb.quiz.find_one({"_id": ObjectId(quiz_id), "quiz_type": "j4"})
        quiz_list = json.dumps(quiz, default=str, ensure_ascii=False)
        result = json.loads(quiz_list)
        return jsonify(result), 200
    else:
        return jsonify({"status": 200}), 200


# 단어 목록 퀴즈 정답 제출 및 결과 저장
def list_quiz_answer(user_id, quiz_id, answer):
    quiz = mongodb.quiz.find_one({"_id": ObjectId(quiz_id), "quiz_type": "j4"})
    example = quiz.get("example")
    correct = 0
    result = {}
    for ex in quiz.get("example"):
        if ex in answer:
            result[ex] = 1
            correct += 1
        else:
            result[ex] = 0
    if quiz.get("number") < 2:
        mongodb.quiz_result.insert_one(
            {"quiz_id": quiz_id, "user_id": user_id, "correct": correct, "number": quiz.get("number") + 1,
             "quiz_type": "j4", "result": result, "date" : quiz.get("date")})
        random.shuffle(example)
        mongodb.quiz.update_one({"_id": ObjectId(quiz_id), "quiz_type": "j4"},
                                {"$set": {"number": quiz.get("number") + 1, "example": example}})
        return True
    else:
        mongodb.quiz_result.insert_one(
            {"quiz_id": quiz_id, "user_id": user_id, "correct": correct, "number": quiz.get("number") + 1,
             "quiz_type": "j4", "result": result, "date" : quiz.get("date")})
        return False

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

    quizList = json.dumps(user, default=str, ensure_ascii=False)
    result = json.loads(quizList)
    return jsonify(result), 200


# 퀴즈 다시 풀기
@app.route("/quiz/retry/answer", methods=['POST'])
def retry_answer():
    quiz_id = request.json.get('quiz_id')
    my_answer = request.json.get('answer')
    quiz = mongodb.quiz.find_one({'_id': ObjectId(quiz_id)})
    user_id = quiz.get('user_id')
    quiz_type = quiz.get('quiz_type')

    if quiz_type == "j4":
        quiz_length = len(list(mongodb.quiz_result.find({'quiz_id': quiz_id})))
        example = quiz.get('example')
        correct = 0
        result = {}
        for i in example:
            result[i] = 0
            if i in my_answer:
                correct += 1
                result[i] = 1
        data = {
            'quiz_id': quiz_id,
            'user_id': user_id,
            'correct': correct,
            'number': quiz_length + 1,
            'quiz_type': "j4",
            'result': result
        }
        mongodb.quiz_result.insert_one(data)
    elif quiz_type == "j3":
        answer = quiz.get('answer')
        if my_answer == answer:
            mongodb.quiz_result.update_one({'quiz_id': quiz_id}, {'$set': {'correct': 1, 'my_answer': my_answer}})
    return jsonify({"status": 200}), 200


# 퀴즈 시작하기
@app.route("/quiz/start", methods=['POST'])
def quiz_start():
    user_id = request.json.get('user_id')
    date = request.json.get('date')
    category = mongodb.categories.find_one({'user_id': user_id})
    news_lst = category.get("current_news_id_lst")

    quiz_create(user_id, news_lst, date)

    quiz_lst = mongodb.quiz.find_one({"user_id": user_id, "quiz_type": "j3", "date": date})

    # return quiz_lst

    quizList = json.dumps(quiz_lst, default=str, ensure_ascii=False)
    result = json.loads(quizList)
    return jsonify(result), 200


def quiz_create(user_id, news_lst, date):
    content_sum = ""
    result = {}
    cnt = 1
    for news in news_lst:
        # 디테일 불러오기
        data = send_detail_request(news)
        content_sum += data.get("return_object").get("documents")[0].get("content")
        # 단답형 문제 생성
        answer, question = question_generator(data.get("return_object").get("documents")[0].get("content"))
        # 4지선다 이야기 회상형 퀴즈 생성
        dict1 = create_choice_quiz(user_id, data.get("return_object").get("documents")[0].get("content"), answer,
                                   question, date)
        result[str(cnt)] = dict1
        cnt += 1

    # 비동기
    Thread(target=quiz_list, args=(content_sum, user_id, date)).start()

    doc = {'user_id': user_id, "quiz_type": "j3", "date": date, "result": result}
    mongodb.quiz.insert_one(doc)

# j6 불러오기 GET
@app.route("/quiz/start/j6", methods=['GET'])
def quiz_get_j6():
    user_id = request.json.get('user_id')
    date = request.json.get('date')
    quiz = mongodb.quiz.find_one({"user_id": user_id, "quiz_type": "j6", "date": date})
    # return quiz_lst
    quizList = json.dumps(quiz, default=str, ensure_ascii=False)
    result = json.loads(quizList)
    return jsonify(result), 200

# j6 풀기 POST
@app.route("/quiz/start/j6", methods=['POST'])
def quiz_solve_j6():
    body = request.json
    user_id = body.get("user_id")
    quiz_id = body.get("quiz_id")
    answer = body.get("answer")

    quiz = mongodb.quiz.find_one({"_id": ObjectId(quiz_id), "quiz_type": "j6"})
    example = quiz.get("example")
    correct = 0
    result = {}
    for ex in example:
        if ex in answer:
            result[ex] = 1
            correct += 1
        else:
            result[ex] = 0

    mongodb.quiz_result.insert_one(
        {"quiz_id": quiz_id, "user_id": user_id, "correct": correct, "number": quiz.get("number") + 1,
         "quiz_type": "j6", "result": result, "date" : quiz.get("date")})

    return jsonify({"status": 200}), 200


# 단어 퀴즈 생성 함수
def quiz_list(content_sum, user_id, date):
    # 키워드 추출
    keywords = get_keywords(content_sum, 10)
    # 단어 목록 퀴즈 생성
    create_word_list_quiz(user_id, keywords, date)
    # 단어 목록 퀴즈 생성
    create_word_list_quiz_z6(user_id, keywords, date)
    # 단어 목록 20 퀴즈 생성
    create_word_list2_quiz(user_id, keywords, date)


# j4 불러오기
@app.route("/quiz/start/j4", methods=['POST'])
def quiz_start_j4():
    user_id = request.json.get('user_id')
    date = request.json.get('date')
    quiz = mongodb.quiz.find_one({"user_id": user_id, "quiz_type": "j4", "date": date})

    # return quiz_lst

    quizList = json.dumps(quiz, default=str, ensure_ascii=False)
    result = json.loads(quizList)
    return jsonify(result), 200



# j7 불러오기
@app.route("/quiz/start/j7", methods=['POST'])
def quiz_start_j7():
    user_id = request.json.get('user_id')
    date = request.json.get('date')
    quiz = mongodb.quiz.find_one({"user_id" : user_id, "quiz_type" : "j7", "date": date})

    # return quiz_lst

    quizList = json.dumps(quiz, default=str, ensure_ascii=False)
    result = json.loads(quizList)
    return jsonify(result), 200



# j7 정답 제출
@app.route("/quiz/asnwer/j7", methods=['POST'])
def answer_j7():
    user_id = request.json.get('user_id')
    quiz_id = request.json.get("quiz_id")
    answer_o = request.json.get("answer_o")
    answer_x = request.json.get("answer_x")
    quiz_answer_j7(user_id, quiz_id, answer_o, answer_x)
    return jsonify({"status":200}), 200


# j7 정답 처리 및 결과 저장

def quiz_answer_j7(user_id, quiz_id, answer_o, answer_x):
    quiz = mongodb.quiz.find_one({"_id": ObjectId(quiz_id), "quiz_type": "j7"})
    score = 0
    for ans in answer_o:
        if ans in quiz.get("answer"):
            score += 1
    for ans in answer_x:
        if ans not in quiz.get("answer"):
            score +=1
    score -= 10
    if score < 0:
        score = 0

    mongodb.quiz_result.insert_one({"quiz_id": quiz_id, "user_id": user_id, "score": score, "quiz_type": "j7", "date" : quiz.get("date")})
    score_save(user_id, quiz.get("date"))


def score_save(user_id, date):
    j3 = mongodb.quiz_result.find_one({"user_id": user_id, "quiz_type":"j3", "date":date})
    j3_score = j3.get("correct")*10
    j4_lst = mongodb.quiz_result.find({"user_id": user_id, "quiz_type":"j4", "date":date})
    j4_score = 0
    for j4 in j4_lst:
        j4_score += j4.get("correct")

    j6 = mongodb.quiz_result.find_one({"user_id": user_id, "quiz_type":"j6", "date":date})
    j6_score = j6.get("correct")

    j7 = mongodb.quiz_result.find_one({"user_id": user_id, "quiz_type":"j7", "date":date})
    j7_score = j7.get("score")

    j9_score =8.15+5.5+j3_score+j4_score+6.85+j6_score+j7_score+1.75
    dict1 = {
        "j1":8.15,
        "j2":5.5,
        "j3":j3_score,
        "j4":j4_score,
        "j5":6.85,
        "j6":j6_score,
        "j7":j7_score,
        "j8":1.75,
        "j9":j9_score
    }
    print(dict1)
    mongodb.score.update_one({'user_id': user_id}, {"$set": {"date": {date: dict1}}}, upsert=True)





@app.route("/quiz/myscore", methods=['POST'])
def my_score():
    body = request.json
    user_id = body.get("user_id")
    score = mongodb.score.find_one({"user_id":user_id})
    average = mongodb.score.find_one({"user_id": "평균"})

    data = {
        "user_id": score.get("user_id"),
        "average": average.get("date").get("average"),
        "date": score.get("date")

    }

    scores = json.dumps(data, default=str, ensure_ascii=False)
    result = json.loads(scores)
    return jsonify(result), 200



# 서버 올릴 때 설정
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
