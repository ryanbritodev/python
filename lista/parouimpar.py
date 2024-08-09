print("PROGRAMA PAR OU ÍMPAR")

while True:
    try:
        # Código que pode causar uma exceção
        numero = int(input("Digite um número inteiro e descubra se ele é par ou ímpar: ").strip())
        break
    except ValueError:
        # Código para tratar a exceção ValueError
        print("Erro! Por favor, insira um número inteiro válido.")


if numero % 2 == 0:
    print(f"O número {numero} é par!")
else:
    print(f"O número {numero} é ímpar!")
