import collections

data = open('hightemp.txt', 'r')
lines = data.readlines()
lines = [line.split()[0] for line in lines]

counter = collections.Counter(lines)

for word in counter:
    print(word)
