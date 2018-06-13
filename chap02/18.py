data = open('hightemp.txt', 'r')
lines = data.readlines()

temp = [line.split()[3] for line in lines]
print(sorted(temp, reverse=True))
