print("FUNÇÃO QUE SOMA DOIS VALORES")

while True:
    try:
        def soma(num1, num2):
            return print(f"SOMA = {num1 + num2}")
            # Tudo antes do return é executado


        valor = float(input("Digite o valor 1: "))
        valor2 = float(input("Digite o valor 2: "))

        soma(valor, valor2)
        break

    except ValueError:
        print("Erro! Tente novamente")
