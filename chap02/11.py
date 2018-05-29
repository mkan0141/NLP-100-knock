data = open('hightemp.txt')
for line in data:
    print(line.replace('\t', ' '), end='')
