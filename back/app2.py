import datetime

from flask import Flask, jsonify, request
import requests
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_connect = "mongodb+srv://admin:1234@cluster0.zyylgba.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_connect)
mongodb = client.brain

file_path = "category.json"

app = Flask(__name__)

@app.route("/user/myQuiz", methods=['POST'])
def my_quiz():
    user_id = request.json.get('user_id')
    user = list(mongodb.quiz.find({'user_id': user_id}))

    print(user)
    quizList = json.dumps(user, default=str, ensure_ascii=False)
    return quizList

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
