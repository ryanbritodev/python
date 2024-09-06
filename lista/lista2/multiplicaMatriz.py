# Exercício 1: Multiplicação de Matrizes
# Escreva uma função chamada multiplica_matrizes(matriz1, matriz2) que recebe duas matrizes como entrada e retorna a matriz resultante da multiplicação dessas duas matrizes.

m1 = [
    [2, 4, 5],
    [2, 5, 7],
    [6, 8, 1]
]

m2 = [
    [6, 7, 3],
    [3, 2, 9],
    [5, 9, 6]
]

def condicaoMatrizes(m1, m2):
    contador = 0
    if len(m1) == len(m2):
        for matriz in m1:
            if len(matriz) != len(m2[contador]):
                return "Matrizes inválidas"
            else:
                contador += 1
                continue
        return "Matrizes válidas"
    else:
        return "Matrizes inválidas"

def multiplicaMatriz(m1, m2):
    if condicaoMatrizes(m1, m2) == "Matrizes inválidas":
        return "Ímpossível multiplicar as matrizes"
    else:
        matriz = 0
        indiceMatriz = 0
        indice = 0
        tamanhoMatriz = len(m1)
        cont = 1
        matrizMult = []
        while cont <= tamanhoMatriz:
            matrizMult.append([])
            cont += 1
        while True:
            indice = 0
            while indice < len(m1[0]):
                matrizMult[indiceMatriz].append(m1[indiceMatriz][indice] * m2[indiceMatriz][indice])
                indice += 1
            indiceMatriz += 1
            if indiceMatriz == tamanhoMatriz:
                break
        return matrizMult

print(multiplicaMatriz(m1, m2))
