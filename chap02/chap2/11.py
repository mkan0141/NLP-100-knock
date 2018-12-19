data = open('hightemp.txt').readlines()
data = [d.replace('\t', ' ') for d in data]

for i in data:
    print(i, end='')
