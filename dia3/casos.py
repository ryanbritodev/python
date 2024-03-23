print("CONDIÇÕES DE UM NÚMERO")

numero = int(input("Digite o valor do número: "))
resto = numero % 2

# IF ALINHADO - SÓ EXECUTA SE O PRIMEIRO CONDICIONAL FOR VERDADEIRO E O SEGUNDO TAMBÉM

if resto == 0:
    if numero < 100:
        print("Seu número é par e menor que 100.")

if resto == 0:
    if numero >= 100:
        print("Seu número é par e maior ou igual a 100.")

if resto > 0:
    if numero < 100:
        print("Seu número é ímpar e menor que 100.")

if resto > 0:
    if numero >= 100:
        print("Seu número é ímpar e maior ou igual a 100.")
