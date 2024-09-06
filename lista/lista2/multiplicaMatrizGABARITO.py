# GABARITO
def multiplica_matrizes(m1, m2):
    # Verifica se as matrizes podem ser multiplicadas
    if len(m1[0]) != len(m2):
        return "Impossível multiplicar as matrizes"

    # Inicializa a matriz resultante com zeros
    resultado = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]

    # Multiplicação de matrizes
    for i in range(len(m1)):  # Para cada linha de m1
        for j in range(len(m2[0])):  # Para cada coluna de m2
            for k in range(len(m2)):  # Para cada elemento na linha de m1 e coluna de m2
                resultado[i][j] += m1[i][k] * m2[k][j]

    return resultado


# Exemplo de uso
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

resultado = multiplica_matrizes(m1, m2)
print("Matriz resultante da multiplicação:")
for linha in resultado:
    print(linha)
