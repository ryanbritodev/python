num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
a = num1
soma = 0

while a <= num2:
    if a % 2 == 0:
        soma += a
    a += 1

print(soma)
