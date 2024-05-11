def soma(a, b):
    print(f"RESULTADO: {a + b}")
    return


def divisao(a, b):
    print(f"RESULTADO: {a / b}")
    return


def mult(a, b):
    print(f"RESULTADO: {a * b}")
    return


def sub(a, b):
    print(f"RESULTADO: {a - b}")
    return


print("------- CALCULADORA -------")

while True:
    try:
        operacao = input("Digite a operação desejada (X, /, +, -): ")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro! Tente novamente!")

while True:
    try:
        if operacao == "+":
            soma(num1, num2)
            break
        elif operacao == "-":
            sub(num1, num2)
            break
        elif operacao == "X":
            mult(num1, num2)
            break
        elif operacao == "/":
            divisao(num1, num2)
            break
    except ValueError:
        print("Erro! Tente novamente!")
