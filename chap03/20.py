import json

def select_title(word):
    data =open('jawiki-country.json', 'r').readlines()
    return [json.loads(line) for line in data if json.loads(line)['title'] == word]

data = select_title('イギリス')

for d in data:
    print(d, end='')
