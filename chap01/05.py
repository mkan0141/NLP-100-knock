def n_gram(sentence, n):
    s_list = []
    for i in range(len(sentence) - 1):
        s_list.append(sentence[i] + sentence[i+1])
    return s_list

sentence = "I am an NLPer"

print(n_gram(sentence, 2))
print(n_gram(sentence.split(' '), 2))
