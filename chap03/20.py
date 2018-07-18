import json

data =open('jawiki-country.json', 'r')
text = data.readlines()

for a in text:
    if json.loads(a)['title'] == 'イギリス':
        print(json.loads(a)['text'])


