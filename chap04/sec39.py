from sec30 import mapping
from collections import defaultdict
import matplotlib.pyplot as plt

if __name__ == '__main__':
    dic_list = mapping()

    dic = defaultdict(int)
    for d in dic_list:
        dic[d['surface']] += 1

    data = [value for key, value in sorted(dic.items())]
    rank = list(range(1, len(data) + 1))
    print(data)
    data.sort(reverse=True)
    plt.plot(rank, data, '.')
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
