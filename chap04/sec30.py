def mapping():
    dic_list = []
    with open('neko.txt.mecab') as f:
        for morpheme in f.readlines():
            morpheme = morpheme.split('\t')
            if len(morpheme) >= 2:
                morpheme_info = morpheme[1].split(',')
                morpheme = morpheme[0]
                dic = {
                    'surface' : morpheme,
                    'base'    : morpheme_info[6],
                    'pos'     : morpheme_info[0],
                    'pos1'    : morpheme_info[1]
                }
                dic_list.append(dic)
    return dic_list

if __name__ == '__main__':
    dic_list = mapping()
    print(dic_list)