import sys

args = sys.argv

data = open('hightemp.txt').readlines()

for i in range(int(args[1])):
    print(data[i].replace('\n', ''))

