from __future__ import absolute_import, print_function
from tweepy import OAuthHandler, Stream, StreamListener
import re
import time
import json
# Enter Twitter API Keys
# http://apps.twitter.com 
consumer_key="gAJAEIYlILzQuCpdEDKnIeLrj"
consumer_secret="xHpwWfCFeHGAKFc6w94Kk5TFsWqlgYcqt82v1sFqbY0yYMt9am"
access_token="1382217118658142211-uTL6uM6alWIAlCmErC12zuY3xQOAAI"
access_token_secret="vTqn2fUSwH31aRDsS3kYvDKLuLEQZIGmtfDL57E1ba92N"


# Initialize Global variable
tweet_count = 0
# Input number of tweets to be downloaded
n_tweets = 100

key_word = ["covid-19", "coronavirus", "covid19", "covid", "virus", "social distance", "social distancing", "self-quarantine", "self quarantine"]
#key_word = ["food", "yummy", "delicious"]
#key_word = ["a", "b", "c", "d"]

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        global tweet_count
        global n_tweets
        global stream

        if tweet_count < n_tweets:
            temp_data = json.loads(data)
            for word in key_word:
                if word in temp_data["text"].lower():
                    print(data)
                    tweet_count += 1
                    return True
        else:
            time.sleep(1)
            tweet_count = 0

    def on_error(self, status):
        time.sleep(10)
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    #stream.filter(locations=[109.59,-44.55,159.34,-11.05], is_async=True) 
    #track = ['COVID-19', 'coronavirus', 'hospital']
    #locations=[109.59,-44.55,159.34,-11.05]
    stream.filter(locations=[109.59,-44.55,159.34,-11.05],languages=['en'], is_async=True)
    #stream.filter(locations=[109.59,-44.55,159.34,-11.05],languages=['en'], is_async=True)
