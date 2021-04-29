import json


text_list = []


with open("word.txt", 'r') as f:
    for line in f:
        line = line.strip('\t').strip()
        text_list.append(line)

count = 1
with open("tweets.json", 'r', encoding="utf-8") as f:
    for line in f:
        line = line.rstrip()
      
        is_in = False
        line = json.dumps(line)
        

        data = json.loads(line)
        text = data.split('"text":')[-1]
        text = data.split(',"display_text_range":')[0]

        text = text.lower().split()
        
     
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
