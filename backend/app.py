#!flask/bin/python
import redis
from flask import Flask, jsonify, make_response
import couchdb
from flask_cors import CORS
from utils import view_reformatter
from utils import getTop3VulgarWords
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

URL_vulgarWordFreq = 'language/vulgarWordFreq'
URL_vulgarWordFreqAU = 'language/vulgarWordFreqAU'
URL_hashtagFreq = 'language/hashtagFreq'
URL_hashtagFreqAU = 'language/hashtagFreqAU'
URL_countTweetByStates = 'language/countTweetByStates'

# Get rows of views
vulgarWordFreq = view_reformatter(vulgardb.view(URL_vulgarWordFreq, group=True).rows,
                                  URL_vulgarWordFreq) # vulgar word frequency in each state
vulgarWordFreqTop3 = view_reformatter(getTop3VulgarWords(
                                vulgardb.view(URL_vulgarWordFreq, group=True).rows),
                                URL_vulgarWordFreq) # top3 vulgar word frequency in each state
vulgarWordFreqAU = view_reformatter(vulgardb.view(URL_vulgarWordFreqAU, group=True).rows,
                                    URL_vulgarWordFreqAU) # vulgar word frequency in australia
vulgar_viewHashtagFreq = view_reformatter(vulgardb.view(URL_hashtagFreq, group=True).rows,
                            URL_hashtagFreq) # hashtag frequency in vulgar tweets from each state
clean_viewHashtagFreq = view_reformatter(cleandb.view(URL_hashtagFreq, group=True).rows,
                            URL_hashtagFreq) # hashtag frequency in clean tweets from each state
vulgar_viewHashtagFreqAU = view_reformatter(vulgardb.view(URL_hashtagFreqAU, group=True).rows,
                            URL_hashtagFreqAU) # hashtag frequency in vulgar tweets in australia
clean_viewHashtagFreqAU = view_reformatter(cleandb.view(URL_hashtagFreqAU, group=True).rows,
                            URL_hashtagFreqAU) # hashtag frequency in clean tweets in australia
vulgar_countTweetByStates = vulgardb.view(URL_countTweetByStates, group=True) # vulgar tweet count in each state
clean_countTweetByStates = vulgardb.view(URL_countTweetByStates, group=True) # clean tweet count in each state

mocks_scenario2 = {
    "title":['State', 'TOP1', 'TOP2', 'TOP3'],
    "WA": ['WA(word1,word2,word3)', 127, 111, 10],
    "QLD": ['QLD(word1,word2,word3)', 111, 100, 1],
    "NT": ['NT(word1,word2,word3)', 127, 111, 10],
    "NSW": ['NSW(word1,word2,word3)', 127, 111, 10],
    "VIC": ['VIC(word1,word2,word3)', 127, 111, 10],
    "TAS": ['TAS(word1,word2,word3)', 127, 111, 10],
}

@app.route('/scenario2', methods=['GET'])
def get_scenario_two():
    return jsonify(mocks_scenario2)

@app.route('/scenario3', methods=['GET'])
def get_scenario_three():
    return jsonify(vulgarWordFreqAU)

@app.route('/scenario4/vulgar', methods=['GET'])
def get_scenario_four_vulgar():
    return jsonify(vulgar_viewHashtagFreq)

@app.route('/scenario4/clean', methods=['GET'])
def get_scenario_four_clean():
    return jsonify(clean_viewHashtagFreq)

# Error Handling
@app.errorhandler(400)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
