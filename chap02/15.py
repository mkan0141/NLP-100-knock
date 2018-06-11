data = open('hightemp.txt')

n = int(input())

for x in data.readlines()[-1:-n:-1]:
    print(x.rstrip())
