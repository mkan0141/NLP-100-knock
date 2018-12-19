data = open('hightemp.txt', 'r').readlines()
print(len(set([i[0] for i in data])))
