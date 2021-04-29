import json


text_list = []


with open("word.txt", 'r') as f:
    for line in f:
        line = line.strip('\t').strip()
        text_list.append(line)

id_list = []
with open("tweets.json", 'r', encoding="utf-8") as f:
    for line in f:
        line = line.rstrip()
      
        is_in = False
        line = json.dumps(line)
        

        data = json.loads(line)
        text = data.split('"text":',1)[-1]
        text = text.split(',"source":"')[0]
        text = text.lower().split()
        
        id_str = data.split('"id_str":',1)[-1]
        id_str = id_str.split(',"text":')[0]
        
        if (id_str in id_list):
        	continue

        for i in range(len(text)):
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