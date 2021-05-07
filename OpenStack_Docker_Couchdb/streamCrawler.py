import tweepy
import json
import couchdb
import time
server = couchdb.Server('http://admin:12345@127.0.0.1:5984/')

db = server['tweets']


print("___________")
consumer_key = "gAJAEIYlILzQuCpdEDKnIeLrj"
consumer_secret = "xHpwWfCFeHGAKFc6w94Kk5TFsWqlgYcqt82v1sFqbY0yYMt9am"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token = "1382217118658142211-uTL6uM6alWIAlCmErC12zuY3xQOAAI"
access_token_secret = "vTqn2fUSwH31aRDsS3kYvDKLuLEQZIGmtfDL57E1ba92N"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        d = status._json
        d["_id"] = status.id_str

        doc_id,doc_rev = db.save(d)
        print (doc_id,doc_rev)

    def on_error(self, status_code):
        print(status_code,"error")
        return True # Don't kill the stream

    def on_timeout(self):
        print("timeout")
        return True # Don't kill the stream
while True:
    try:
        sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
        sapi.filter(locations=[112.78,-44.0,154.18,-11.4])
    except:
        print("error")
        time.sleep(30)
