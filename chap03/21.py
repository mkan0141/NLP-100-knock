import json
import re

def select_title(word):
    data =open('jawiki-country.json', 'r').readlines()
    return [json.loads(line)['text'] for line in data if json.loads(line)['title'] == word]


data = select_title('イギリス')
regix = '.*Category.*'
pattern = re.compile(regix)

data = pattern.findall(''.join(data))
for d in data:
    print(d)
