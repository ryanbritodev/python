colunasELinhas = str(input("Informe a quantidade de colunas e linhas desejadas: ")).replace(" ", "").replace("X", "").replace("x", "")
colunas = int(colunasELinhas[0])
linhas = int(colunasELinhas[1])
def criaMatriz(colunas, linhas):
    matriz = []
    for j in range(linhas):
        linha = []
        for i in range(colunas):
            linha.append(int(input(f"Insira o {i + 1}° valor da linha {j + 1}: ")))
        matriz.append(linha)
    return matriz

matriz = criaMatriz(5, 4)
