str1 = 'パトカあああー'
str2 = 'タクシー'

str3 = ''

for a,b in zip(str1,str2):
    str3 += a
    str3 += b
print(str3)
