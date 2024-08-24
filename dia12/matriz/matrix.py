colunas = int(input("Quantas colunas deseja para sua matriz? "))
linhas = int(input("Quantas linhas deseja para sua matriz? "))

matriz = []

def criaMatriz(colunas, linhas):
    for j in range(linhas):
        linha = []
        for i in range(colunas):
            linha.append(int(input(f"Insira o {i + 1}° valor da linha {j + 1}: ")))
        matriz.append(linha)
    return matriz

def printarMatriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(f"{valor:.0f}", end=" ")
        print()

matriz = criaMatriz(colunas, linhas)
printarMatriz(matriz)