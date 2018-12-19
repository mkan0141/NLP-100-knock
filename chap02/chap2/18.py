data = open('hightemp.txt', 'r').readlines()
data.sort(key = lambda x: -float(x.split()[2]))
for i in data:
    print(i, end='')
