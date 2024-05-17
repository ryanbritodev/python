num = int(input("Digite o número de repetições: "))
i = 1
limite = 1

while limite <= num:
    i = 1
    while i <= limite:
        print(i, end=" ")
        i += 1
    print()

    limite += 1
