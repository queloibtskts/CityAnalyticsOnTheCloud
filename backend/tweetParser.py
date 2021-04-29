import couchdb

from tweetAnalyser import tweetTagger

admin_username = "admin"
admin_password = "12354"
vic_database = 'vic_tweet'
nsw_database = 'nsw_tweet'
test_database = 'ccc_twitter_test5'

server = couchdb.Server()
server.resource.credentials = (admin_username, admin_password)
test_db = server[test_database]

locations = ['melbourne', 'perth', 'sydney']
explicit_perc = {}  # count explicit tweets
for loc in locations:
    explicit_perc[loc] = {}
    URL = '_design/location/_view/' + loc  # views created in GUI
    view = test_db.view(URL)
    explicit_perc[loc]['total_rows'] = view.total_rows  # emitted tweets from map functions
    
    count = 0
    explicit = 0
    clean = 0
    for row in view.rows:
        tw = row['key']
        
        tagger = tweetTagger(tw)
        tag = tagger.analyseTweet(tw)
        
        count += 1
        
        if tag['vulgar_words']:
            explicit += 1
        else:
            clean += 1
    assert count==view.total_rows
    # print(f'In {loc}: number of explicit tweets: {explicit}\tnumber of clean tweets: {clean}')
    explicit_perc[loc]['n_explict'] = explicit

print(f'Final output: {explicit_perc}')