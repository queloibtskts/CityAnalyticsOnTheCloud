import json
import tweepy
import json
import couchdb

def connect_to_database(database_name, server):
    try:
        return server[database_name]
    except:
        return server.create(database_name)


server = couchdb.Server('http://admin:12345@172.26.131.136:5984/')

# db = server['tweets'] 
database1 = 'vulgar_tweet_by_search2'
database2 = 'clean_tweet_by_search2'

db1 = connect_to_database(database1, server)
db2 = connect_to_database(database2, server)

def save_partitionly(data, db):
    state_abbrevsAndNames = {'ACT': 'ACT', 'VIC': 'Victoria', 'NSW': 'New South Wales',
                             'NT': 'Northern Territory', 'QLD': 'Queensland', 'TAS': 'Tasmania',
                             'WA': 'Western Australia', 'SA': 'South Australia'}
    for (k, v) in state_abbrevsAndNames.items():
        if (data['place'] and data['place']['full_name']) \
            and ((k in data['place']['full_name']) or (v.lower() in data['place']['full_name'].lower())):
            data['_id'] = k + ':' + data['id_str']
            db.save(data)
            return 0

with open("tag_tweets_keyword.json", 'r') as f:
    for line in f:
        data = json.loads(line)
        if(data["tag"]["vulgar_words"] == "True"):
            try:
                save_partitionly(data, db1)
            except:
                print('jump: ', data['id_str'])
        elif(data["tag"]["vulgar_words"] == "False"):
            try:
                save_partitionly(data, db2)
            except:
                print('jump: ', data['id_str'])

