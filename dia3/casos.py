print("CONDIÇÕES DE UM NÚMERO")

numero = int(input("Digite o valor do número: "))

if numero % 2 == 0:
    if numero < 100:
        print("Seu número é par e menor que 100.")

if numero % 2 == 0:
    if numero >= 100:
        print("Seu número é par e maior ou igual a 100.")

if numero % 1 == 0:
    if numero < 100:
        print("Seu número é ímpar e menor que 100.")

if numero % 1 == 0:
    if numero >= 100:
        print("Seu número é par e maior ou igual a 100.")
