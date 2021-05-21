import json

id_list = []
duplicate = []
with open('tag_tweets_keyword.json', 'r') as f:
    for line in f:
        data = json.loads(line)
        id_str = data['id_str']

        if(id_str in id_list):
            duplicate.append(id_str)
            continue
        else:
            if(len(id_list) >= 1000000):
                id_list.clear()
            id_list.append(id_str)
            
        data = json.dumps(data)
        print(data)
    print(duplicate)


