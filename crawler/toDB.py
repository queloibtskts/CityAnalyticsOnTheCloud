import json
import tweepy
import json
import couchdb

def connect_to_database(database_name, server):
    try:
        return server[database_name]
    except:
        return server.create(database_name)


server = couchdb.Server('http://admin:12345@mycouchdb:5984/')

# db = server['tweets'] 
database1 = 'vulgar_tweet_by_search'
database2 = 'clean_tweet_by_search'

db1 = connect_to_database(database1, server)
db2 = connect_to_database(database2, server)



with open("temp.json", 'r') as f:
    for line in f:
        data = json.loads(line)
        if(data["tag"]["vulgar_words"] == "True"):
            db1.save(data)
        elif(data["tag"]["vulgar_words"] == "False"):
            db2.save(data)
