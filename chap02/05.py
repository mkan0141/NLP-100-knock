def n_gram(sentence, n):
    return [sentence[i:i+n] for i in range(len(sentence) - n + 1)]

sentence = "I am an NLPer"
print(n_gram(sentence.split(' '), 2))
