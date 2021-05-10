import tweepy
import json
import couchdb
#from streaming_to_couchdb import connect_to_database
import preprocessor as p
p.set_options(p.OPT.URL, p.OPT.MENTION)  # remove URL and mentions in tweet text

## set API connection
consumer_key = "gAJAEIYlILzQuCpdEDKnIeLrj"
consumer_secret = "xHpwWfCFeHGAKFc6w94Kk5TFsWqlgYcqt82v1sFqbY0yYMt9am"
access_token = "1382217118658142211-uTL6uM6alWIAlCmErC12zuY3xQOAAI"
access_token_secret = "vTqn2fUSwH31aRDsS3kYvDKLuLEQZIGmtfDL57E1ba92N"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)

database1 = 'vulgar_tweet_by_search'
database2 = 'clean_tweet_by_search'

def connect_to_database(database_name, server):
    try:
        return server[database_name]
    except:
        return server.create(database_name)

# uncomment 5 lines below to connect to local db server
# server = "localhost:5984"
# admin_username = "admin"
# admin_password = "12354"
# server = couchdb.Server()
# server.resource.credentials = (admin_username, admin_password)

# connect to remote db server
server = couchdb.Server('http://admin:12345@127.0.0.1:5984/')

db1 = connect_to_database(database1, server)
db2 = connect_to_database(database2, server)

#date_since = "2020-04-21"
geocode = '-26.4391,133.2813,2079km'
SINCE = "2021-05-05"
UNTIL = "2021-05-06"

text_list = []

with open(
        "swear_word.txt",
        'r') as f:
    for line in f:
        line = line.strip('\t').strip()
        text_list.append(line)

id_list = []
tweets = api.search(q = "", geocode = geocode, lang = "en", result_type = "recent",
                    since = SINCE, until = UNTIL, count = 999999)
# print(tweets)
# if tweets != None:
if len(tweets)!=0:
    for tweet in tweets:
        is_in = False
        vulgar_words_used = []
        data = json.dumps(tweet._json)
        data_json = json.loads(data)
        text = data_json['text']
        text = p.clean(text)
        text = text.lower().split()
        # print(text)
        
        id_str = json.loads(data)['id_str']
        
        for i in range(len(text)):
            if (id_str in id_list):
                continue
            
            if ((text[i] + ' ' + text[(i + 1) % len(text)] + ' ' + text[(i + 2) % len(text)] + ' ' +
                 text[(i + 3) % len(text)] + ' ' + text[
                     (i + 4) % len(text)]) in text_list):
                is_in = True
                vulgar_words_used.append(text[i] + ' ' + text[(i + 1) % len(text)] + ' ' + text[(i + 2) % len(text)] + ' ' +text[(i + 3) % len(text)] + ' ' + text[(i + 4) % len(text)])
            
            elif ((text[i] + ' ' + text[(i + 1) % len(text)] + ' ' + text[
                (i + 2) % len(text)] + ' ' + text[
                       (i + 3) % len(text)]) in text_list):
                vulgar_words_used.append(text[i] + ' ' + text[(i + 1) % len(text)] + ' ' + text[(i + 2) % len(text)] + ' ' + text[(i + 3) % len(text)])
                is_in = True
            

            elif ((text[i] + ' ' + text[(i + 1) % len(text)] + ' ' + text[
                (i + 2) % len(text)]) in text_list):
                is_in = True
                vulgar_words_used.append(text[i] + ' ' + text[(i + 1) % len(text)] + ' ' + text[(i + 2) % len(text)])
            

            elif ((text[i] + ' ' + text[(i + 1) % len(text)]) in text_list):
                is_in = True
                vulgar_words_used.append(text[i] + ' ' + text[(i + 1) % len(text)])

            elif ((text[i]) in text_list):
                is_in = True
                vulgar_words_used.append(text[i])
        
        if is_in:
            data_json['tag'] = {'vulgar_words': "True", 'vulgar_words_used': vulgar_words_used}
            db1["tweet:%d" % data_json['id']] = data_json
        else:
            data_json['tag'] = {'vulgar_words': "False", 'vulgar_words_used': vulgar_words_used}
            db2["tweet:%d" % data_json['id']] = data_json
        
        id_list.append(id_str)

else:
    print("Cannot search tweets\n")
