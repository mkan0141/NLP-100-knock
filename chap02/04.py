index_list = [1,5,6,7,8,9,15,16,19]
str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'.replace('.','').split(' ')

ans = []
for index,x in enumerate(index_list):
    if x + 1 in index_list:
        ans.append(str[x][:1])
    else:
        ans.append(str[x][:2])
print(ans)

