def leMatriz(linhas, colunas):
    matriz = []
    for j in range(linhas):
        linha = []
        for i in range(colunas):
            linha.append(int(input(f"Matriz[{j}][{i}]: ")))
        matriz.append(linhas)
    return matriz

print(leMatriz(3, 3))
