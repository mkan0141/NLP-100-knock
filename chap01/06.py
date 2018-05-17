def n_gram(sentence, n):
    return [sentence[i:i+n] for i in range(len(sentence))]

X = n_gram("paraparaparadise", 2)
Y = n_gram("paragraph", 2)

set_X = set(X)
set_Y = set(Y)

print(set_X.union(set_Y))
print(set_X.intersection(set_Y))
print(set_X.difference(set_Y))

print("se" in set_X.intersection(set_Y))
