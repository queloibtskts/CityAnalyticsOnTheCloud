'''Detect and collect vulgar words from tweet text from different locations;
return percentages of vulgar tweets'''

import couchdb
import preprocessor as p
import json

#from tweetAnalyser import TweetCensor

admin_username = "admin"
admin_password = "12354"
vic_database = 'vic_tweet'
nsw_database = 'nsw_tweet'
test_database = 'ccc_twitter_test5'

server = couchdb.Server()
server.resource.credentials = (admin_username, admin_password)
test_db = server[test_database]

PATH_VULGAR_WORD = '../crawler/swear_word.txt' # 'profanity-list.txt'

def read_vulgar_words_file(PATH_VULGAR_WORD):
    f = open(PATH_VULGAR_WORD, 'r')
    vulgar_list = []
    for l in f:
        vulgar_list.append(f.readline().strip())
    f.close()
    
    for vulword in vulgar_list:
        # flatten vulgar_list
        if ':' in vulword:
            # vulword is a root-variant pair
            vulgar_list.remove(vulword)
            root, variant = vulword.split(':')
            vulgar_list.append(root)
            if ',' in variant:
                # variants is a list of variants of a vulgar word
                variant = variant.split(',')
                vulgar_list.extend(variant)
            else:
                vulgar_list.append(variant)
    return vulgar_list

class TweetCensor:
    
    def __init__(self, raw_tweet, vulgar_list):
        self.tweet_text = self.clean_tweet_text(raw_tweet['text'])
        self.vulgar_words = vulgar_list
        self.detect_vulgar_words()
    
    def clean_tweet_text(self, tx):
        p.set_options(p.OPT.URL, p.OPT.MENTION)  # remove URL and mentions in tweet text
        tx = p.clean(tx)
        return tx
    
    def detect_vulgar_words(self):
        vulword_appeared = []  # (unique) vulgar words appeared in the text
        for vulword in self.vulgar_words:
            if vulword in self.tweet_text:
                vulword_appeared.append(vulword)
        return list(set(vulword_appeared))
    
vulgar_list = read_vulgar_words_file(PATH_VULGAR_WORD)

#locations = ['melbourne', 'perth', 'sydney']
locations = ['victoria', 'newsouthwales', 'queensland', 'tasmania', 'westernaustralia',
             'southaustralia', 'northernterritory', 'act', 'jervisbayterritory']
explicit_perc = {}  # count explicit tweets
for loc in locations:
    explicit_perc[loc] = {}
    URL = '_design/location/_view/' + loc  # views created in GUI
    view = test_db.view(URL)
    explicit_perc[loc]['total_rows'] = view.total_rows  # emitted tweets from map functions
    
    count = 0
    explicit = 0
    clean = 0
    for row in view.rows:
        tw = row['key']
        tw_id_str = tw['id_str'] # str
        doc = test_db['tweet:'+tw_id_str]
        
        # tagger = tweetTagger(tw)
        # tag = tagger.analyseTweet(tw)
        # row['tag'] = tag

        censor = TweetCensor(tw, vulgar_list)
        vulword_appeared = censor.detect_vulgar_words()
        doc['vulgar_words'] = vulword_appeared
        test_db[doc.id] = doc # update doc
        count += 1

        # if tag['vulgar_words']:
        if len(vulword_appeared) != 0:
            #print(vulword_appeared)
            explicit += 1
        else:
            clean += 1
    assert count==view.total_rows
    # print(f'In {loc}: number of explicit tweets: {explicit}\tnumber of clean tweets: {clean}')
    explicit_perc[loc]['n_explict'] = explicit

print(f'Final output: {explicit_perc}')
with open('count_vulgar_tweets_byState.json', 'w') as outfile:
    json.dump(explicit_perc, outfile)



