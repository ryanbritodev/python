lista = [12, 25, 37, 39, 41, 53, 59, 68, 71, 95]


# def buscaBinaria(l, v):
#     metadeLista = len(l) // 2
#     for i in range(0, metadeLista):
#         if lista[i] == v:
#             return "Valor encontrado"
#         else:
#             for j in range(metadeLista, len(l)):
#                 if lista[j] == v:
#                     return "Valor encontrado"
#
#
# print(buscaBinaria(lista, 13))


def busca(lis, valor):
    inicial = 0
    final = len(lis) - 1
    while inicial <= final:
        meio = (final + inicial) // 2
        if valor > lis[meio]:
            inicial = meio + 1
        elif valor < lis[meio]:
            final = meio - 1
        elif valor == lis[meio]:
            return meio
    return -1


print(busca(lista, 53))
