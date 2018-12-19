col1 = open('col1.txt').readlines()
col2 = open('col2.txt').readlines()

with open('merge.txt', 'w') as f:
    for x, y in zip(col1, col2):
        f.write(x.replace('\n', '') + '\t' + y.replace('\n', '') + '\n')
