numero = int(input("Digite um número que você deseja saber seus antecessores pares: "))
a = 1

while a < numero:
    if a % 2 == 0:
        print(a)
    a += 1
