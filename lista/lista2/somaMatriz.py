from random import randint as ri

# Exercício 3: Soma de Matrizes
# Escreva uma função chamada soma_matrizes(matriz1, matriz2) que soma duas matrizes de mesma dimensão.
#
# Instruções:
#
# As matrizes de entrada serão de dimensão m x n.
# Verifique se as matrizes têm a mesma dimensão.
# Retorne a matriz resultante da soma.



matriz1 = [
    [ri(1, 10), ri(1, 10), ri(1, 10)],
    [ri(1, 10), ri(1, 10), ri(1, 10)],
    [ri(1, 10), ri(1, 10), ri(1, 10)]
]

matriz2 = [
    [ri(1, 10), ri(1, 10), ri(1, 10)],
    [ri(1, 10), ri(1, 10), ri(1, 10)],
    [ri(1, 10), ri(1, 10), ri(1, 10)]
]

def soma_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2):
        for matrizes in matriz1:
            tamanhoMatriz = []
            tamanhoMatriz.append(len(matrizes))