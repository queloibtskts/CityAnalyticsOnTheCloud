#!flask/bin/python
import redis
from flask import Flask, jsonify, make_response
import couchdb
from flask_cors import CORS
from utils import view_reformatter
cache = redis.Redis(host='redis', port=6379)

app = Flask(__name__)
CORS(app)

# couch db auth
# PORT = "localhost:5984"
# PORT = "127.0.0.1:5984"

# couch db auth
# ADMIN_USERNAME = 'admin'
# ADMIN_PASSWORD = '12345'
server = couchdb.Server('http://admin:12345@127.0.0.1:5984/')
# may change 127.0.0.1 to 172.26.134.127

def connect_to_database(database_name, server):
    try:
        return server[database_name]
    except:
        return server.create(database_name)

DBNAME = 'try'
db = connect_to_database(DBNAME, server)

view = db.view('designDocName/viewName', group=True) # e.g. URL = 'language/vulgarWordFreq'

@app.route('/scenario3', methods=['GET'])
def get_scenario_three():
    return jsonify(view_reformatter(view.rows))

# Error Handling
@app.errorhandler(400)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/samples', methods=['GET'])
def get_samples():
    return jsonify({'dbname': db._name + 'successful!'})

# samples = {
#     "VIC": [
#       {
#         "text": "VICvulgar1",
#         "value": 100
#       },
#       {
#         "text": "VICvulgar2",
#         "value": 100
#       }
#     ],
#     "QL": [
#       {
#         "text": "QLvulgar2",
#         "value": 100
#       },
#       {
#         "text": "QLvulgar2",
#         "value": 100
#       }
#     ],
#     "WA": [
#       {
#         "text": "WAvulgar2",
#         "value": 100
#       },
#       {
#         "text": "WAvulgar2",
#         "value": 100
#       }
#     ],
#     "NSW": [
#       {
#         "text": "NSWvulgar2",
#         "value": 100
#       },
#       {
#         "text": "NSWvulgar2",
#         "value": 100
#       }
#     ],
#     "NT": [
#       {
#         "text": "NTvulgar2",
#         "value": 100
#       },
#       {
#         "text": "NTvulgar2",
#         "value": 100
#       }
#     ],
#     "TAS": [
#       {
#         "text": "TASvulgar2",
#         "value": 100
#       },
#       {
#         "text": "TASvulgar2",
#         "value": 40
#       }
#     ]
# }

if __name__ == '__main__':
    app.run()
