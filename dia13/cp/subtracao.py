# Matriz A e B
from tamanhomatriz import *

def subtracao(a, b):
    # if len(a) == len(b) and len(a[0]) == len(b[0]):
    if tam(a)[0] == tam(b)[0] and tam(a)[1] == tam(b)[1]:
        c = []
        for j in range(len(a)):
            linha = []
            for i in range(len(a[0])):
                linha.append(a[j][i] - b[j][i])
            c.append(linha)
        return c
    else:
        return None

a = [
    [5, 3],
    [2, 1]
]

b = [
    [1, 1],
    [1, 1]
]

print(subtracao(a, b))
