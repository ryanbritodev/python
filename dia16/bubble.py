lista = [5, 8, 3, 2, 9, 1, 7, 4, 6]

for j in range(len(lista) - 1, 1, -1):
    for i in range(j):
        if lista[i] > lista[i + 1]:
            valorAntigo = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = valorAntigo
        print(lista)

# for j, i in enumerate(lista):
#     if i != lista[-1]:
#         indice = lista.index(i)
#         # print(f"Iteração {j + 1}")
#         # print(i)
#         # print(lista[j+1])
#         if i > lista[j+1]:
#             valorAntigo = lista[indice]
#             lista[indice] = lista[j+1]
#             lista[j+1] = valorAntigo
#     else:
#         break
