data = open("hightemp.txt", 'r')
n = int(input())
file_counter = 0

lists = []

for line in data:
    lists.append(line)
    
    if len(lists) == n:
        with open('split_file_' + str(file_counter), 'w') as f:
            for line in lists:
                f.writelines(line)
        file_counter += 1
        lists = []

if len(lists):
    with open('split_file_' + str(file_counter), 'w') as f:
        for line in lists:
            f.writelines(line)
