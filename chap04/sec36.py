from sec30 import mapping
from collections import defaultdict

if __name__ == '__main__':
    dic_list = mapping()

    dic = defaultdict(int)
    for d in dic_list:
        dic[d['surface']] += 1
    dic = sorted(dic.items(), key=lambda x : x[1], reverse=True)

    for i in dic:
        print(i)