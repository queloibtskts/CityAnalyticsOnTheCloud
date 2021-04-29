import tweepy
import json


## set API connection
consumer_key="gAJAEIYlILzQuCpdEDKnIeLrj"
consumer_secret="xHpwWfCFeHGAKFc6w94Kk5TFsWqlgYcqt82v1sFqbY0yYMt9am"
access_token="1382217118658142211-uTL6uM6alWIAlCmErC12zuY3xQOAAI"
access_token_secret="vTqn2fUSwH31aRDsS3kYvDKLuLEQZIGmtfDL57E1ba92N"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
    
api = tweepy.API(auth, wait_on_rate_limit=True)   


date_since = "2020-04-21"
geocode = '-26.4391,133.2813,2079km'
since = "2021-04-21"
until = "2021-04-22"


text_list = []
with open("word.txt", 'r') as f:
    for line in f:
        line = line.strip('\t').strip()
        text_list.append(line)


id_list = []
tweets = api.search(q = "",  geocode=geocode, lang="en", result_type="recent", since= "2021-04-21",until="2021-04-22", count=999999)
if tweets != None:
    for tweet in tweets:
        is_in = False
        data = json.dumps(tweet._json)
        text = json.loads(data)['text']
        text = text.lower().split()
        
        id_str = json.loads(data)['id_str']
        for i in range(len(text)):
            if (id_str in id_list):
                continue

            if((text[i]+' '+text[(i+1)%len(text)]+' '+text[(i+2)%len(text)]+' '+text[(i+3)%len(text)]+' '+text[(i+4)%len(text)]) in text_list and is_in==False):
                print(data)
                is_in = True
            elif((text[i]+' '+text[(i+1)%len(text)]+' '+text[(i+2)%len(text)]+' '+text[(i+3)%len(text)]) in text_list and is_in==False ):
                print(data)
                is_in = True
            elif((text[i]+' '+text[(i+1)%len(text)]+' '+text[(i+2)%len(text)]) in text_list and is_in==False ):
                print(data)
                is_in = True
            elif((text[i]+' '+text[(i+1)%len(text)]) in text_list and is_in==False ):
                print(data)
                is_in = True
            elif((text[i]) in text_list and is_in==False):
                print(data)
                is_in = True
        id_list.append(id_str)

else:
	print("Cannot search tweets\n")
   
