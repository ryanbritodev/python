n = int(input("Digite a quantidade de números da sequência de fibonacci você deseja somar: "))
soma = 0

if n == 0 or n == 1:
    print(0)
else:
    a1 = 0
    a2 = 1

    i = 1

    soma = a1 + a2

    while i <= n - 2:
        fibo = a1 + a2
        a1 = a2
        a2 = fibo
        soma += fibo
        i += 1

print(f"O valor da soma dos números da sequência é {soma}.")
