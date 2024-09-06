def matrizEsparsa(matriz):
    listaZero = []
    listaNum = []
    for matrizes in matriz:
        for linha in matriz:
            for elemento in linha:
                if elemento == 0:
                    listaZero.append(elemento)
                else:
                    listaNum.append(elemento)
    if not matriz:
        return None
    elif len(listaZero) > len(listaNum):
        return "Matriz esparsa"
    else:
        return "Matriz normal"


a = [
    [1, 0, 3],
    [0, 1, 0],
    [1, 0, 1]
]

print(matrizEsparsa(a))
