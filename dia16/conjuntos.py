# Estrutura do Tipo Conjunto
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {6, 2, 8, 4, 10}
conjuntoTupla = set((1, 2, 3, 4, 5))
conjuntoLista = set([1, 2, 3, 4, 5])
print(conjunto)
print(type(conjunto))

c = conjunto - conjunto2
d = conjunto & conjunto2
e = conjunto | conjunto2

print(c)
print(d)
print(e)

# Set não admite repetição de dados


