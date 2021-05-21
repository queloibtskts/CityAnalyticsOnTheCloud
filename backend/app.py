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

vulgarDBNAME = 'vulgar_tweet_by_search'
vulgardb = connect_to_database(vulgarDBNAME, server)

cleanDBNAME = 'clean_tweet_by_search'
cleandb = connect_to_database(cleanDBNAME, server)

vulgarWordFreq = vulgardb.view('language/vulgarWordFreq', group=True)

mocks_scenario2 = {
    "title":['State', 'TOP1', 'TOP2', 'TOP3'],
    "WA": ['WA(word1,word2, word3)', 127, 111, 10],
    "QLD": ['QLD(word1,word2, word3)', 111, 100, 1],
    "NT": ['NT(word1,word2, word3)', 127, 111, 10],
    "NSW": ['NSW(word1,word2, word3)', 127, 111, 10],
    "VIC": ['VIC(word1,word2, word3)', 127, 111, 10],
    "TAS": ['TAS(word1,word2, word3)', 127, 111, 10],
}

@app.route('/scenario2', methods=['GET'])
def get_scenario_two():
    return jsonify(mocks_scenario2)

vulgarWordFreqAU = vulgardb.view('language/vulgarWordFreqAU', group=True)

@app.route('/scenario3', methods=['GET'])
def get_scenario_three():
    return jsonify(view_reformatterAU(vulgarWordFreqAU.rows))

vulgar_viewHashtagFreq = vulgardb.view('language/hashtagFreq', group=True)
clean_viewHashtagFreq = cleandb.view('language/hashtagFreq', group=True)

@app.route('/scenario4/vulgar', methods=['GET'])
def get_scenario_four_vulgar():
    return jsonify(view_reformatter(vulgar_viewHashtagFreq.rows))

@app.route('/scenario4/clean', methods=['GET'])
def get_scenario_four_clean():
    return jsonify(view_reformatter(clean_viewHashtagFreq.rows))
# Error Handling
@app.errorhandler(400)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
