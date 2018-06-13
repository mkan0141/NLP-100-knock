data = open('hightemp.txt', 'r')
lines = data.readlines()


col1 = [i.split('\t')[0] for i in lines]
col1_set = set(col1)

print(col1_set)
