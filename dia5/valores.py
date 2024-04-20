quantidade = int(input("Digite a quantidade de valores desejados: "))
a = 1
soma = 0

while a <= quantidade:
    valor = float(input(f"Digite o valor {a}: "))
    a += 1
    soma = soma + valor

media = soma / quantidade
print(f"A média dos valores é: {media:.2f}")
