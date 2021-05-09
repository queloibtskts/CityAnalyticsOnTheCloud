import tweepy
import json
import couchdb
import time
server = couchdb.Server('http://admin:12345@127.0.0.1:5984/')

db = server['tweets']


consumer_key = "gAJAEIYlILzQuCpdEDKnIeLrj"
consumer_secret = "xHpwWfCFeHGAKFc6w94Kk5TFsWqlgYcqt82v1sFqbY0yYMt9am"
access_token = "1382217118658142211-uTL6uM6alWIAlCmErC12zuY3xQOAAI"
access_token_secret = "vTqn2fUSwH31aRDsS3kYvDKLuLEQZIGmtfDL57E1ba92N"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)



text_list = []

with open("swear_word.txt", 'r') as f:
    for line in f:
        line = line.strip('\t').strip()
        text_list.append(line)






class CouchDBStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        try:
            text = json.loads(data)['text']
            text = text.lower().split()

            for i in range(len(text)):
                if((text[i]+' '+text[(i+1)%len(text)]+' '+text[(i+2)%len(text)]+' '+text[(i+3)%len(text)]+' '+text[(i+4)%len(text)]) in text_list):
                    doc_id,doc_rev = db.save(data)
                    print (doc_id,doc_rev)
                    break
                elif((text[i]+' '+text[(i+1)%len(text)]+' '+text[(i+2)%len(text)]+' '+text[(i+3)%len(text)]) in text_list):
                    doc_id,doc_rev = db.save(data)
                    print (doc_id,doc_rev)
                    break
                elif((text[i]+' '+text[(i+1)%len(text)]+' '+text[(i+2)%len(text)]) in text_list):
                    doc_id,doc_rev = db.save(data)
                    print (doc_id,doc_rev)
                    break
                elif((text[i]+' '+text[(i+1)%len(text)]) in text_list):
                    doc_id,doc_rev = db.save(data)
                    print (doc_id,doc_rev)
                    break
                elif((text[i]) in text_list):
                    doc_id,doc_rev = db.save(data)
                    print (doc_id,doc_rev)
                    break
                    
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
        stream.filter(locations=[110.01,-45.02,160.82,-12.02],languages=['en'])
    except:
        print("error")
        time.sleep(30)