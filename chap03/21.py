import json

data = open('jawiki-country.json', 'r')
text = data.readlines()

data = [json.loads(a) for a in text if json.loads(a)['title'] == 'イギリス']

for d in data:
    if 'Category' in d['text']:
        print(d['text'])
