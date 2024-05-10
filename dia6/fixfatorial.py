n = int(input("Digite o valor do fatorial desejado: "))
fatorial = 1
i = 1

while i <= n:
    fatorial *= i
    i += 1

print(fatorial)
