lista = [5, 8, 3, 2, 9, 1, 7, 4, 6]

for i in range(len(lista) - 1, 1, -1):
    for j in range(i):
        if lista[j] > lista[j + 1]:
            valorAntigo = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = valorAntigo

print(lista)
