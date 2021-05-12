#!flask/bin/python
import redis
from flask import Flask, jsonify, make_response
import couchdb
from flask_cors import CORS
cache = redis.Redis(host='redis', port=6379)
# pip install couchdb

app = Flask(__name__)
CORS(app)

# couch db auth
# host = localhost:5984
# database = 'ccc_twitter_test'
# admin_username = "admin"
# admin_password = "12345"
# connect to couch db
# s = couchdb.Server('http://{admin_username}:{admin_password}@{url}/')

# cache = s[database]

# URL = '_design/twitterInfo/_view/twitter'
# view = cache.view(URL)
# row_number = view.total_rows

# @app.route('/scenario2', methods=['GET'])
# def get_scenario_one():
#     return jsonify(explicit_perc)

@app.route('/scenario3', methods=['GET'])
def get_scenario_two():
    return jsonify({'row_number': 1})

# Error Handling
@app.errorhandler(400)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/v1/samples', methods=['GET'])
def get_samples():
    return jsonify({'samples': samples})

samples = [
    {
        'id': 1,
        'location': u'Melbourne',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Sydney',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

if __name__ == '__main__':
    app.run()
