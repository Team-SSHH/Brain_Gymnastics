from datetime import date, timedelta

from flask import Flask, jsonify, request
import requests
from flaskext.mysql import MySQL
from pymongo import MongoClient
import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer

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

# cursor.execute("SELECT * from User")
# data = cursor.fetchone()
# print(data)

mongo_connect = "mongodb+srv://admin:1234@cluster0.zyylgba.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_connect)
mongodb = client.brain


# 카테고리 별 뉴스 보기
@app.route("/news/category", methods=['POST'])
def news():
    body = request.json
    data = {
        "access_key": "9f7da60c-c993-459a-88c7-9a4230797087",
        "argument": {
            "query": "",
            "published_at": {
                "from": body['from'],
                "until": body['until']
            },
            "provider": [
            ],
            "category": body['category'],
            "category_incident": [
            ],
            "byline": "",
            "provider_subject": [
            ],
            "subject_info": [
                ""
            ],
            "subject_info1": [
                ""
            ],
            "subject_info2": [
                ""
            ],
            "subject_info3": [
                ""
            ],
            "subject_info4": [
                ""
            ],
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

    return jsonify(data), 200


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
                # news_id
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