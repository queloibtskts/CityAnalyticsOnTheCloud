import couchdb
from utils_dataAnalysis import *  # Ugh.. "unresolved reference" error maybe an IDE issue

server = couchdb.Server('http://admin:12345@127.0.0.1:5984/') # may change 127.0.0.1 to 172.26.134.127
# if reduce_overflow_error: set config -> query_server_config -> reduce_limit to false in GUI
# if timeout error: set config -> couchdb -> os_process_timeout to 50000 or larger in GUI

vulgarDBNAME = 'vulgar_tweet_by_search'
vulgardb = connect_to_database(vulgarDBNAME, server)

cleanDBNAME = 'clean_tweet_by_search'
cleandb = connect_to_database(cleanDBNAME, server)

URL_vulgarWordFreq = 'language/vulgarWordFreq'
URL_countTweetByStates = 'language/countTweetByStates'

# Get rows of views
vulgarWordFreqTop3 = getTop3VulgarWords(
    vulgardb.view(URL_vulgarWordFreq, group=True).rows
)  # top3 vulgar word frequency in each state
vulgar_countTweetByStates = vulgardb.view(URL_countTweetByStates, group=True
                                          )  # vulgar tweet count in each state
clean_countTweetByStates = cleandb.view(URL_countTweetByStates, group=True
                                         )  # clean tweet count in each state

# create csv for Tableau visualisation
top3VulgarWordsJson_to_CSV(vulgarWordFreqTop3, vulgar_countTweetByStates)
countTweetsByStateJson_to_CSV(clean_countTweetByStates, vulgar_countTweetByStates)
countTweetsByStateJson_to_CSV2(clean_countTweetByStates, vulgar_countTweetByStates)
