tupla = 1, 2, 3
print(f"Tupla: {tupla}\n")

add = []

while True:
    valor = int(input("Digite um valor para adicionar na tupla ou 999 pra sair: "))
    if valor == 999:
        break
    else:
        add.append(valor)
        novaTupla = tuple(add)
        tuplaAdd = tupla + novaTupla
        print(tuplaAdd)

novaTupla = tuple(add)
tuplaAdd = tupla + novaTupla

print(f"\nTupla com valores adicionados:\n{tuplaAdd}\n")

while True:
    tuplaAdd = list(tuplaAdd)
    valor = int(input("Digite um valor para remover da tupla ou 999 pra sair: "))
    if valor in tuplaAdd:
        indice = tuplaAdd.index(valor)
        del tuplaAdd[indice]
        print(tuple(tuplaAdd))
    elif valor == 999:
        break
    else:
        print("Valor não encontrado!")

print(f"\nTupla com valores removidos:\n{tuplaAdd}\n")
