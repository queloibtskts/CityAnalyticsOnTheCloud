import base64
import requests
#import couchdb
import time
import json


province = "australia"
#geocode = '-29.1425,133.1389,2081km'
geocode = '-25.2744,133.7751,2081km'


since = "2021-04-19"
until = "2021-04-20"
query =""

consumer_key="gAJAEIYlILzQuCpdEDKnIeLrj"
consumer_secret="xHpwWfCFeHGAKFc6w94Kk5TFsWqlgYcqt82v1sFqbY0yYMt9am"
access_token="1382217118658142211-uTL6uM6alWIAlCmErC12zuY3xQOAAI"
access_token_secret="vTqn2fUSwH31aRDsS3kYvDKLuLEQZIGmtfDL57E1ba92N"

temp_key = '{}:{}'.format(consumer_key, consumer_secret).encode('ascii')
b64_encoded_key = base64.b64encode(temp_key)
b64_encoded_key = b64_encoded_key.decode('ascii')
#################################################################
#################################################################

auth_url = 'https://api.twitter.com/oauth2/token'

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}

auth_data = {'grant_type': 'client_credentials'}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

access_token = auth_resp.json()['access_token']

header = { 'Authorization': 'Bearer {}'.format(access_token) }
url = 'https://api.twitter.com/1.1/search/tweets.json'

def search_tweets(query, province, geocode, since, until, headers):
      while True:
          try:
              search_content = {
                  'q': "",
                  'geocode': geocode,
                  'since': since,  # 7 days only
                  'until': until,
                  'count': 100,  # max 100 with free api
                  'result_type': 'recent',  # mixed, recent, popular
                  #'max_id': str(tweet_id),
                  'retryonratelimit': True
              }

              result = requests.get(url, headers=header, params=search_content)
              tweets = result.json()['statuses']

              if len(tweets) != 0:
                  for tweet in tweets:
                      try:
                          data = json.dumps(tweet)
                          print(data)
                      except Exception as e:
                          print(e)
              else:
                  print("Tweets does not exist\n")
                  break

          except Exception as e:
              print(e)
              print("rating limit, Sleep for a while\n")
              time.sleep(888)  # sleep 

search_tweets(query, province, geocode, since, until, header)
