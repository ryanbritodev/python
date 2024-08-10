lista = list()

while True:
    n = float(input("Digite um número: "))
    lista.append(n)
    flag = str(input("Deseja adicionar mais algum elemento? [S/N] ")).strip().upper()
    while flag != "S" and flag != "N":
        print("Opção inválida! Tente novamente")
        flag = str(input("Deseja adicionar mais algum elemento? [S/N] ")).strip().upper()
    if flag == "S":
        continue
    else:
        break

soma = 0

for valor in lista:
    soma += valor

print(f"A média dos elementos é {soma / len(lista):.2f}")
