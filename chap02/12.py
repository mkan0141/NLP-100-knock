data = open('hightemp.txt')
col1 = open('col1.txt', 'w')
col2 = open('col2.txt', 'w')

for x in data.readlines():
    col1.write(x[0])
    col2.write(x[1])
