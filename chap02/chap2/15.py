import sys
args = sys.argv
n = int(args[1])

data = open('hightemp.txt', 'r').readlines()
for i in data[-n:]:
    print(i, end='')
