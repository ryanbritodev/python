# Matrizes e objetos multidimensionais são generalizações de objetos simples vistos anteriormente (listas)
# Esses tipos de dados nos permitem armazenar informações mais complexas em uma única variável
# Processamento de imagens, localização, jogos de tabuleiro,
# Matrizes são bidimensionais, sendo formadas por listas, todas do mesmo tamanho

def matrizValida(matriz):
    if not matriz:
        return "Matriz inválida"
    tamanho_linha = len(matriz[0])
    for linha in matriz:
        if len(linha) != tamanho_linha:
            return "Matriz inválida"
    return "Matriz válida"

def printarMatriz(matriz):
    if not matrizValida(matriz):
        print("Matriz não existe")
        return
    for linha in matriz:
        for valor in linha:
            print(f"{valor:.0f}", end=" ")
        print()

matriz = [
    [3, 7, 1],
    [0, 9, 2],
    [2, 1, 1]
]

print(matrizValida(matriz))
printarMatriz(matriz)
