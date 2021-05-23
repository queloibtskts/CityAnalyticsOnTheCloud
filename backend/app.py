#!flask/bin/python
import redis
from flask import Flask, jsonify, make_response
import couchdb
from flask_cors import CORS
from utils_ import *  # Ugh.. "unresolved reference" error maybe an IDE issue
cache = redis.Redis(host='redis', port=6379)

app = Flask(__name__)
CORS(app)

# server = couchdb.Server('http://admin:12345@127.0.0.1:5984/') # may change 127.0.0.1 to 172.26.134.127
# # if reduce_overflow_error: set config -> query_server_config -> reduce_limit to false in GUI
# # if timeout error: set config -> couchdb -> os_process_timeout to 50000 or larger in GUI

# couch db auth
# ADMIN_USERNAME = 'admin'
# ADMIN_PASSWORD = '12345'
server = couchdb.Server('http://admin:12345@mycouchdb:5984/') #use docker - can not connect to couchdb
# may change 127.0.0.1 to 172.26.134.127

vulgarDBNAME = 'vulgar_tweet_by_search'
vulgardb = connect_to_database(vulgarDBNAME, server)

cleanDBNAME = 'clean_tweet_by_search'
cleandb = connect_to_database(cleanDBNAME, server)

# URL_vulgarWordFreq = 'language/vulgarWordFreq'
URL_vulgarWordFreqAU = 'language/vulgarWordFreqAU'
URL_hashtagFreq = 'language/hashtagFreq'
# URL_hashtagFreqAU = 'language/hashtagFreqAU'

# Get rows of views
# vulgarWordFreq = view_reformatter(vulgardb.view(URL_vulgarWordFreq, group=True).rows,
#                                   URL_vulgarWordFreq)  # vulgar word frequency in each state
# vulgarWordFreqTop3 = getTop3VulgarWords(
#     vulgardb.view(URL_vulgarWordFreq, group=True).rows
# )  # top3 vulgar word frequency in each state
vulgarWordFreqAU = view_reformatter(vulgardb.view(URL_vulgarWordFreqAU, group=True).rows,
                                    URL_vulgarWordFreqAU)  # vulgar word frequency in australia
vulgar_viewHashtagFreq = view_reformatter(vulgardb.view(URL_hashtagFreq, group=True).rows,
                                          URL_hashtagFreq, isRemovingNonAscii=True
                                          )  # hashtag frequency in vulgar tweets from each state
clean_viewHashtagFreq = view_reformatter(cleandb.view(URL_hashtagFreq, group=True).rows,
                                         URL_hashtagFreq, isRemovingNonAscii=True
                                         )  # hashtag frequency in clean tweets from each state
# vulgar_viewHashtagFreqAU = view_reformatter(vulgardb.view(URL_hashtagFreqAU, group=True).rows,
#                             URL_hashtagFreqAU, isRemovingNonAscii = True) # hashtag frequency in vulgar tweets in australia
# clean_viewHashtagFreqAU = view_reformatter(cleandb.view(URL_hashtagFreqAU, group=True).rows,
#                             URL_hashtagFreqAU, isRemovingNonAscii = True) # hashtag frequency in clean tweets in australia


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
