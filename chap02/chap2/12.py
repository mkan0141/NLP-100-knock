data = open('hightemp.txt', 'r')
col1 = open('col1.txt', 'w')
col2 = open('col2.txt', 'w')

for x in data.readlines():
    col1.write(x.rstrip().split()[0] + '\n')
    col2.write(x.rstrip().split()[1] + '\n')
