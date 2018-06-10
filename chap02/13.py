col1 = open('col1.txt', 'r')
col2 = open('col2.txt', 'r')
output = open('col3.txt', 'w')

for (a,b) in zip(col1,col2):
    output.write(a.rstrip() + '\t '+ b.rstrip() + '\n')
