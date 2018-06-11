data = open('hightemp.txt', 'r')
n = int(input())
for x in data.readlines()[:n]:
    print(x.strip())
