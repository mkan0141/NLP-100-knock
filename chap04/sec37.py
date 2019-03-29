from sec30 import mapping
from collections import defaultdict
import matplotlib.pyplot as plt

if __name__ == '__main__':
    dic_list = mapping()

    dic = defaultdict(int)
    for d in dic_list:
        dic[d['surface']] += 1
    top_ten = sorted(dic.items(), key=lambda x : x[1], reverse=True)[0:10]
    print(list(top_ten))

    left = [x[0] for x in top_ten]
    height = [x[1] for x in top_ten]
    plt.rcParams['font.family'] = 'AppleGothic' 
    plt.bar(left, height)
    plt.show()
    print(left)
