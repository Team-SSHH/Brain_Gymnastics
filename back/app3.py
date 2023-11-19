from flask import Flask, jsonify, request
import requests
from flaskext.mysql import MySQL
import json
from question_generator import question_generator
from threading import Thread
from konlpy.tag import Okt
from pymongo import MongoClient
from bson.objectid import ObjectId
from collections import Counter
import random

mongo_connect = "mongodb+srv://admin:1234@cluster0.zyylgba.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_connect)
mongodb = client.brain


file_path = "category.json"

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'brain'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

# cursor.execute("SELECT * from users")
# data = cursor.fetchone()
# print(data)


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
    news_id = body.get("news_id")

    data = send_detail_request(news_id)

    return jsonify(data), 200


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
          "images",
          # "provider_subject",
          # "provider_news_id",
          # "publisher_code"
        ]
      }
    }
    response = requests.post('https://tools.kinds.or.kr/search/news', json=data)
    data = response.json()
    return data


# 유저가 본 뉴스의 카테고리와 news_id 저장
@app.route("/category/save", methods=['POST'])
def category_save():
    body = request.json
    news_id = body.get('news_id', None)
    category = body.get('category', None)
    user_id = "csi"
    category_cnt(user_id, news_id, category)
    # 비동기
    Thread(target=quiz_create, args=(user_id, news_id)).start()
    return jsonify({"status": 200}), 200


# 카테고리 저장 및 news_id 저장
def category_cnt(user_id, news_id, category_list):
    with open(file_path, "r", encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    categories = json_data.get('category', [])
    for category in categories:
        if category in category_list:
            mongodb.categories.update_one({'user_id': user_id},{'$inc': {f'category.{category}': 1}}, upsert=True)



# 퀴즈 생성 함수
def quiz_create(user_id, news_id):
    quiz = mongodb.quiz.find_one({'news_id': news_id})
    if not quiz:
        data = send_detail_request(news_id)
        keywords = get_keywords(data.get("return_object").get("documents")[0].get("content"), 10)
        answer, question = question_generator(data.get("return_object").get("documents")[0].get("content"))

        create_word_list_quiz(user_id, news_id, keywords)
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

    example = {str(i + 1): choice for i, choice in enumerate(all_choices)}
    answer_number = [key for key, value in example.items() if value == answer][0]

    docdoc = {'user_id': user_id, "quiz_question": question, "example": example, "answer": answer_number, "quiz_type": 1, "news_id": news_id}
    mongodb.quiz.insert_one(docdoc)



def get_keywords(content, n):

    # 형태소 분석기
    okt = Okt()

    # 문장에서 명사 추출
    nouns = okt.nouns(content)

    # 빈도 계산
    count = Counter(nouns)

    # 빈도가 높은 순으로 10개
    top_nouns = [noun for noun, freq in count.most_common(n)]

    return top_nouns


@app.route("/choice/answer", methods=['POST'])
def choice_answer():
    body = request.json
    user_id = body.get("user_id")
    quiz_id = body.get("quiz_id")
    answer = body.get("answer")
    choice_quiz_answer(user_id, quiz_id, answer)

    return jsonify({"status": 200}), 200

def choice_quiz_answer(user_id, quiz_id, answer):
    quiz = mongodb.quiz.find_one({"_id": ObjectId(quiz_id), "quiz_type": 1})
    if quiz.get("answer") == answer:
        mongodb.quiz_result.insert_one({"quiz_id": quiz_id, "user_id": user_id, "correct": 1, "answer":quiz.get("answer"), "quiz_type": 1, "my_answer":answer})
    else:
        mongodb.quiz_result.insert_one({"quiz_id": quiz_id, "user_id": user_id, "correct": 0, "answer":quiz.get("answer"), "quiz_type": 1, "my_answer":answer})


@app.route("/list/answer", methods=['POST'])
def list_answer():
    body = request.json
    user_id = body.get("user_id")
    quiz_id = body.get("quiz_id")
    answer = body.get("answer")
    list_quiz_answer(user_id, quiz_id, answer)

    return jsonify({"status": 200}), 200

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



