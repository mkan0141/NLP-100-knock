import random

input_data = input() 
input_data = input_data.split(' ')
if len(input_data) > 4:
    random.shuffle(input_data)

for ch in input_data:
    print(ch,end=' ')


