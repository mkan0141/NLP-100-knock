data = open('hightemp.txt')
col1 = open('col1.txt', 'w')
col2 = open('col2.txt', 'w')

for x in data.readlines():
    col1.write(x.split()[0] + '\n')
    col2.write(x.split()[1] + '\n')
