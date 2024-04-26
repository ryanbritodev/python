print("NÚMEROS PARES")
print("DIGITE UM NÚMERO E VEJA TODOS OS PARES DE 1 ATÉ ELE")

while True:
    try:
        numero = int(input("Digite o número desejado: ").strip())
        break
    except ValueError:
        print("Número inválido! Tente novamente: ")

i = 2

while i <= numero:
    print(i)
    i += 2
