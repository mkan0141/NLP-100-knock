import MeCab

def create_mecab_file(filename):
    with open(filename, 'r') as data_file, open(filename + '.mecab', 'w') as output_file:
        mecab = MeCab.Tagger()
        output_file.write(mecab.parse(data_file.read()))

if __name__ == '__main__':
    create_mecab_file('neko.txt')
