#!flask/bin/python
import redis
from flask import Flask, jsonify, make_response
import couchdb
from flask_cors import CORS
from utils import view_reformatter
from utils import view_reformatterAU
cache = redis.Redis(host='redis', port=6379)

app = Flask(__name__)
CORS(app)

server = couchdb.Server('http://admin:12345@127.0.0.1:5984/') # may change 127.0.0.1 to 172.26.134.127

def connect_to_database(database_name, server):
    try:
        return server[database_name]
    except:
        return server.create(database_name)

DBNAME = 'vulgar_tweet_by_search'
db = connect_to_database(DBNAME, server)


@app.route('/scenario2', methods=['GET'])
def get_scenario_two():
    return jsonify(mocks_scenario2)

mocks_scenario2 = []

viewVulgarWordFreq = db.view('language/vulgarWordFreq', group=True)

@app.route('/scenario3', methods=['GET'])
def get_scenario_three():
    return jsonify(mocks_cenario3) # view_reformatter(viewVulgarWordFreq.rows)

mocks_cenario3 = {
    "AU": [
      {
        "text": "Cvulgar11",
        "value": 100
      },
      {
        "text": "Cvulgar22",
        "value": 100
      },
      {
        "text": "Cvulgar1",
        "value": 100
      },
      {
        "text": "Cvulgar2s",
        "value": 100
      }
    ],
}

viewHashtagFreqAU = db.view('language/hashtagFreqAU', group=True)

@app.route('/scenario4', methods=['GET'])
def get_scenario_four():
    return jsonify(view_reformatterAU(viewHashtagFreqAU.rows))

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

if __name__ == '__main__':
    app.run()
