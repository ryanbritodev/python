lista = [1, 2, 3, 50, 100]


def busca(listagem, item):
    for i in range(len(listagem)):
        if listagem[i] == item:
            return i
    return None


print(busca(lista, 50))
