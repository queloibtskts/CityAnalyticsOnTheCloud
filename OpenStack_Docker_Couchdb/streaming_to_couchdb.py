import tweepy
import json
import couchdb
import time
import preprocessor as p
p.set_options(p.OPT.URL, p.OPT.MENTION)  # remove URL and mentions in tweet text

#db = server['tweets']

def connect_to_database(database_name, server):
    try:
        return server[database_name]
    except:
        return server.create(database_name)

database1 = 'vulgar_tweet_by_search'
database2 = 'clean_tweet_by_search'

# uncomment 5 lines below to connect to local db server
# server = "localhost:5984"
# admin_username = "admin"
# admin_password = "12354"
# server = couchdb.Server()
# server.resource.credentials = (admin_username, admin_password)

# connect to remote db server; comment 1 line below if connecting to local db server
server = couchdb.Server('http://admin:12345@mycouchdb:5984/')

db1 = connect_to_database(database1, server)
db2 = connect_to_database(database2, server)


consumer_key = "gAJAEIYlILzQuCpdEDKnIeLrj"
consumer_secret = "xHpwWfCFeHGAKFc6w94Kk5TFsWqlgYcqt82v1sFqbY0yYMt9am"
access_token = "1382217118658142211-uTL6uM6alWIAlCmErC12zuY3xQOAAI"
access_token_secret = "vTqn2fUSwH31aRDsS3kYvDKLuLEQZIGmtfDL57E1ba92N"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)





text_list = []
id_list = []

with open("swear_word.txt", 'r') as f:
    for line in f:
        line = line.strip('\t').strip()
        text_list.append(line)






class CouchDBStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        try:
            id_str = json.loads(data)['id_str']
            if(id_str in id_list):
                return True
            else:
                if(len(id_list) >= 1000000):
                    id_list.clear()

                id_list.append(id_str)

            text = json.loads(data)['text']
            text = p.clean(text)
            text = text.lower().split()
            is_in = False
            vulgar_words_used = []
            for i in range(len(text)):
                if((text[i]+' '+text[(i+1)%len(text)]+' '+text[(i+2)%len(text)]+' '+text[(i+3)%len(text)]+' '+text[(i+4)%len(text)]) in text_list):
                    is_in = True
                    vulgar_words_used.append(text[i]+' '+text[(i+1)%len(text)]+' '+text[(i+2)%len(text)]+' '+text[(i+3)%len(text)]+' '+text[(i+4)%len(text)])

                elif((text[i]+' '+text[(i+1)%len(text)]+' '+text[(i+2)%len(text)]+' '+text[(i+3)%len(text)]) in text_list):
                    is_in = True
                    vulgar_words_used.append(text[i]+' '+text[(i+1)%len(text)]+' '+text[(i+2)%len(text)]+' '+text[(i+3)%len(text)])


                elif((text[i]+' '+text[(i+1)%len(text)]+' '+text[(i+2)%len(text)]) in text_list):
                    is_in = True
                    vulgar_words_used.append(text[i]+' '+text[(i+1)%len(text)]+' '+text[(i+2)%len(text)])


                elif((text[i]+' '+text[(i+1)%len(text)]) in text_list):
                    is_in = True
                    vulgar_words_used.append(text[i]+' '+text[(i+1)%len(text)])


                elif((text[i]) in text_list):
                    is_in = True
                    vulgar_words_used.append(text[i])

            data = json.loads(data)
            if is_in:
                data['tag'] = {'vulgar_words': "True", 'vulgar_words_used': vulgar_words_used}
                db1["tweet:%d" % data['id']] = data # error caused by saving json.dumps(data) to db
                #print(json.dumps(data))
            else:
                data['tag'] = {'vulgar_words': "False", 'vulgar_words_used': vulgar_words_used}
                db2["tweet:%d" % data['id']] = data # error caused by saving json.dumps(data) to db
                #print(json.dumps(data))


        except BaseException as e:
            print("BaseException occurs!!",e)
            print(data)
            return True
        return True

    def on_error(self, status_code):
        print(status_code,"error")
        return True

    def on_timeout(self):
        print("timeout")
        return True
while True:
    try:
        stream = tweepy.streaming.Stream(auth, CouchDBStreamListener())
        stream.filter(locations=[72.25,-55.32,168.23,-9.09],languages=['en'])
    except:
        print("error")
        time.sleep(30)
