#!flask/bin/python
from flask import Flask, jsonify, make_response
# pip install couchdb
import couchdb

app = Flask(__name__)

# couch db auth
database = 'ccc_twitter_test'
server = "localhost:5984"
admin_username = "admin"
admin_password = "12354"

# connect to couch db
server = couchdb.Server()
server.resource.credentials = (admin_username, admin_password)
db = server[database]
# view = db[0]

# @app.route('/api/v1/scenarios', methods=['GET'])
# def get_scenarios():
#     return view

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
