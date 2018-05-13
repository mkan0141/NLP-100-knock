import re

s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

number = [1,5,6,7,8,9,15,16,19]
str_list = re.split('\W+',s)
ans_list = {}

for i in range(len(str_list)):
    if len(str_list[i]) > 0:
        if str_list[i] in number:
            ans_list[str_list[i][0]] = i
        else:
            ans_list[str_list[i][:2]] = i

print(ans_list)



