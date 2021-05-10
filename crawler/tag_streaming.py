from __future__ import absolute_import, print_function
from tweepy import OAuthHandler, Stream, StreamListener
import re
import time
import json
import preprocessor as p
p.set_options(p.OPT.URL, p.OPT.MENTION)  # remove URL and mentions in tweet text
# Enter Twitter API Keys
# http://apps.twitter.com 
# consumer_key="FMdyTPjIpL5wFFRmrnjG1BBNJ"
# consumer_secret="HkQSMpJqH5wr8zg7D5J6inWSl9gFNVV1DcH3M7fvC487TiASLv"
# access_token="2615391175-lkCtIgsZcPBBHWaqdUHRsS4OPrfclhGbwMtJSUo"
# access_token_secret="1OsSZsLgnW4aINLCqJ02UgH0p2gnY2F7pD7gvTzU9H0TO"

consumer_key = "gAJAEIYlILzQuCpdEDKnIeLrj"
consumer_secret = "xHpwWfCFeHGAKFc6w94Kk5TFsWqlgYcqt82v1sFqbY0yYMt9am"
access_token = "1382217118658142211-uTL6uM6alWIAlCmErC12zuY3xQOAAI"
access_token_secret = "vTqn2fUSwH31aRDsS3kYvDKLuLEQZIGmtfDL57E1ba92N"


# Initialize Global variable
tweet_count = 0
# Input number of tweets to be downloaded
n_tweets = 100

#key_word = ["covid-19", "coronavirus", "covid19", "covid", "virus", "social distance", "social distancing", "self-quarantine", "self quarantine", "india", "indian"]
#key_word = ["food", "yummy", "delicious", "kitchen", "cafe", "restaurant"]



text_list = []

def open_txt():
    with open("swear_word.txt", 'r') as f:
        for line in f:
            line = line.strip('\t').strip()
            text_list.append(line)
            


class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            
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
                #db1["tweet:%d" % data['id']] = data
                print(json.dumps(data))
            else:
                data['tag'] = {'vulgar_words': "False", 'vulgar_words_used': vulgar_words_used}
                #db2["tweet:%d" % data['id']] = data
                print(json.dumps(data))


        except BaseException as e:
            print("BaseException occurs!!",e)
            print(data)
            return True
        return True    



    def on_error(self, status):
        time.sleep(10)
        print(status)

if __name__ == '__main__':
    open_txt()
    #print(text_list[0])
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    

    # open file


    stream = Stream(auth, l)
    #stream.filter(locations=[109.59,-44.55,159.34,-11.05], is_async=True) 
    #track = ['COVID-19', 'coronavirus', 'hospital']
    #locations=[109.59,-44.55,159.34,-11.05]
    #stream.filter(locations=[106.698311,-45.075950, 155.949366, -10.755751 ],languages=['en'], is_async=True)
    stream.filter(locations=[110.01,-45.02,160.82,-12.02],languages=['en'], is_async=True)

