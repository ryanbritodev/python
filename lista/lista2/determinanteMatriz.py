# Exercício 2: Determinante de uma Matriz 2x2
# Escreva uma função chamada determinante_matriz_2x2(matriz) que calcula o determinante de uma matriz 2x2.

matriz2X2 = [
    [5, 7],
    [9, 3]
]
def determinanteMatriz2X2(matriz):
    if len(matriz) != 2 or len(matriz[0]) != 2 or len(matriz[1]) != 2:
        return "Impossível determinar o determinante: a matriz não é 2x2"
    else:
        determinante = (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])
        return determinante

print(determinanteMatriz2X2(matriz2X2))
