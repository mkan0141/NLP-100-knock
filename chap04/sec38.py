from sec30 import mapping
from collections import defaultdict
import matplotlib.pyplot as plt

if __name__ == '__main__':
    dic_list = mapping()

    dic = defaultdict(int)
    for d in dic_list:
        dic[d['surface']] += 1

    data = list(dic.values())
    data.sort(reverse=True)
    print(data)
    plt.hist(data, bins=25, range=(0, 50))
    plt.show()
