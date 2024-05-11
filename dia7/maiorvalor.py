num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


def maiorValor(a, b):
    if a > b:
        print(f"O maior número é {a:.0f}")
    elif b > a:
        print(f"O maior número é {b:.0f}")
    else:
        print("Os números são iguais")
    return


maiorValor(num1, num2)
