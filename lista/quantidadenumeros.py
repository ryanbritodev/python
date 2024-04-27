print("QUANTIDADE DE NÚMEROS PARES E ÍMPARES")
print("PROGRAMA PARA CONTAR O NÚMERO DE PARES E ÍMPARES DENTRO DE UM INTERVALO NUMÉRICO")

while True:
    try:
        numero = int(input("Digite o número desejado: ").strip())
        break
    except ValueError:
        print("Número inválido! Tente novamente: ")

i = 1
quantidadePar = 0
quantidadeImpar = 0

while i <= numero:
    if i % 2 == 0:
        quantidadePar += 1
    else:
        quantidadeImpar += 1
    i += 1

print(f"A quantidade de números pares é de {quantidadePar} e de números ímpares é de {quantidadeImpar}")
