from flask import Flask, jsonify, request
import requests
from flaskext.mysql import MySQL
import json
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

    return jsonify(data), 200


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

    return jsonify(data), 200



# 유저가 본 뉴스의 카테고리와 news_id 저장
@app.route("/category/save", methods=['POST'])
def category_save():
    body = request.json
    news_id = body.get('news_id', None)
    category = body.get('category', None)
    user_id = 1
    category_cnt(user_id, news_id, category)
    return 200


# 카테고리 저장 및 news_id 저장
def category_cnt(user_id, news_id, category_list):
    cursor.execute("INSERT INTO user_news (user_id, news_id) VALUES (%s, %s)", (user_id, news_id))
    conn.commit()

    with open(file_path, "r", encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    categories = json_data.get('category', [])
    for category in categories:
        if category in category_list:
            cursor.execute("UPDATE category SET category_cnt = category_cnt + 1 WHERE user_id = %s AND category_name = %s", (user_id, category))
            conn.commit()
            break