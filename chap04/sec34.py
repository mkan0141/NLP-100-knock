from sec30 import mapping

if __name__ == '__main__':
    dic_list = mapping()
    verbs = []
    for i in range(len(dic_list)):
        if dic_list[i]['pos1'] == '連体化':
            verbs.append(dic_list[i - 1]['surface'] + dic_list[i]['surface'] + dic_list[i + 1]['surface'])
    print(verbs)