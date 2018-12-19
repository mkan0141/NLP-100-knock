import json
import re

def select_title(word):
    data =open('jawiki-country.json', 'r').readlines()
    return [json.loads(line)['text'] for line in data if json.loads(line)['title'] == word]


data = select_title('イギリス')
pattern1 = re.compile('\[\[Category:(.*)\]\]')
# pattern2 = re.compile('\]\].*')

data = pattern1.findall('\n'.join(data))
# data = pattern2.sum(data, '')
print(data)
