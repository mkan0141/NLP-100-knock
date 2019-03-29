from sec30 import mapping

if __name__ == '__main__':
    dic_list = mapping()
    nouns = []
    for dic in dic_list:
        if dic['pos'] == '名詞':
            nouns.append(dic['surface'])

    print(nouns) 