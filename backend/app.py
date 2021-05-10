#!flask/bin/python
from flask import Flask, jsonify, make_response
from flask_cors import CORS
# pip install couchdb
import couchdb

app = Flask(__name__)
CORS(app)

# couch db auth
database = 'ccc_twitter_test'
server = "localhost:5984"
admin_username = "admin"
admin_password = "12345"

# connect to couch db
server = couchdb.Server()
server.resource.credentials = (admin_username, admin_password)
db = server[database]

URL = '_design/twitterInfo/_view/twitter'
view = db.view(URL)
row_number = view.total_rows

# @app.route('/api/v1/scenario1', methods=['GET'])
# def get_scenario_one():
#     return jsonify(explicit_perc)

@app.route('/api/v1/scenario2', methods=['GET'])
def get_scenario_two():
    return jsonify({'row_number': row_number})

# @app.route('/api/v1/scenario3', methods=['GET'])
# def get_scenario_three():
#     return jsonify({'row_number': row_number})

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
