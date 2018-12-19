import sys

args = sys.argv
n = int(args[1])
data = open('hightemp.txt', 'r').readlines()

file_cnt = 0
cnt = 0
for i in range(len(data)):
    file_cnt += 1
    f = open('data/hightemp{}.txt'.format(file_cnt), 'w')
    for j in range(n):
        cnt += 1
        f.write(data[i + j])
        if cnt > len(data):
            break
    if cnt > len(data):
        break



