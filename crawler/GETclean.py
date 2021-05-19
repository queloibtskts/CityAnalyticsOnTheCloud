import couchdb
import tweepy
import json
import couchdb
import time
import preprocessor as p
import pandas as pd

def connect_to_database(database_name, server):
    try:
        return server[database_name]
    except:
        return server.create(database_name)

server = couchdb.Server('http://admin:12345@127.0.0.1:5984/')

db = connect_to_database("vulgar_tweet_by_search", server)
#print(db["37c1fde588eef4e9ca254c06b2058579"])
rows = db.view('_all_docs', include_docs=True)
data = [row['doc'] for row in rows]
for i in range(len(data)):
    temp = data[i]
    temp = json.dumps(temp)
    temp = json.loads(temp)
    temp.pop('_id', None)
    temp.pop('_rev', None)
    print(temp)
