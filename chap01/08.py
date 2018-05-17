def cipher(sentence):
    ret = ""
    for c in sentence:
        if c.islower:
            ret += chr(219 - ord(c))
        else:
            ret += c
    return ret

s = "I am e-to student"

x = cipher(s)
print('暗号前: ' + x)

x = cipher(x)
print('暗号後: ' + x)



