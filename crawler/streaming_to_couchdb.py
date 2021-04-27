from __future__ import absolute_import, print_function
import tweepy
from tweepy import OAuthHandler, Stream, StreamListener
import json
# pip install couchdb
import couchdb


# Twitter api auth
consumer_key="gAJAEIYlILzQuCpdEDKnIeLrj"
consumer_secret="xHpwWfCFeHGAKFc6w94Kk5TFsWqlgYcqt82v1sFqbY0yYMt9am"
access_token="1382217118658142211-uTL6uM6alWIAlCmErC12zuY3xQOAAI"
access_token_secret="vTqn2fUSwH31aRDsS3kYvDKLuLEQZIGmtfDL57E1ba92N"

# couch db auth
database = 'ccc_twitter_test'
server = "localhost:5984"
admin_username = "admin"
admin_password = "12354"

locations=[109.59,-44.55,159.34,-11.05] # Australia
filterTerms = ["travel"]
WARNING_COLOUR = '\033[93m'
END_COLOUR = '\033[0m'

class CouchDBStreamListener(StreamListener):
    # ref: https://pmatigakis.wordpress.com/2012/12/01/twitter-data-mining-crawling-twitter/
    def __init__(self, db):
        self.db = db
        self.tweet_count = 0
        self.received_friend_ids = False
    
    def on_data(self, data):
        try:
            tweet = json.loads(data)
        except Exception:
            print(WARNING_COLOUR + "Failed to parse tweet data" + END_COLOUR)
            tweet = None
        
        if tweet:
            if tweet.__contains__('id') and tweet.__contains__("text"):
                print("%s:      %s" % (tweet['user']['screen_name'], tweet['text']))
                
                tweet['doc_type'] = "tweet"
                
                self.db["tweet:%d" % tweet['id']] = tweet
                
                self.tweet_count += 1
            elif not self.received_friend_ids and tweet.__contains__("friends"): #?
                print("Got %d user ids" % len(tweet['friends'])) #?
                self.received_friend_ids = True #?
            else:
                print(WARNING_COLOUR + "Received a response that is not a tweet" + END_COLOUR + " :      " + tweet)
        return True


def main():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    # connect to couch db
    server = couchdb.Server()
    server.resource.credentials = (admin_username, admin_password)
    db = server[database]
    
    listener = CouchDBStreamListener(db)
    
    stream = Stream(auth, listener)
    stream.filter(track = filterTerms, languages = ["en"])
    stream.stream_tweets()

if __name__=="__main__":
    main()