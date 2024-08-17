quant = int(input("Digita a quantidade de termos que você deseja soma: "))

valores = list()

for i in range(1, quant + 1):
    num = int(input(f"Digite o {i}° número: "))
    valores.append(num)


def soma(* valor):
    res = 0
    for l in valor:
        res += l
    return res


print(f"A soma de todos os valores digitados é {soma(*valores)}") # Desempacotamento da lista
