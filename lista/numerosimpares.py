print("NÚMEROS ÍMPARES")
print("DIGITE UM NÚMERO E VEJA TODOS OS ÍMPARES DE 1 ATÉ ELE")

while True:
    try:
        numero = int(input("Digite o número desejado: ").strip())
        break
    except ValueError:
        print("Número inválido! Tente novamente: ")

i = 1

while i <= numero:
    print(i)
    i += 2
