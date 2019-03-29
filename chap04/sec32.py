from sec30 import mapping

if __name__ == '__main__':
    dic_list = mapping()
    verbs = []
    for dic in dic_list:
        if(dic['pos'] == '動詞'):
            verbs.append(dic['base'])

    print(verbs) 
