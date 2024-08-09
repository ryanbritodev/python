# Faça uma função que retorne as raízes de uma equação de segundo grau em que os parâmetros de entrada da função são: a, b, c
a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))
c = int(input("Insira o terceiro número: "))


def bhaskara(a, b, c):
    delta = (b ** 2) - 4 * a * c
    x1 = (-b + (delta ** 0.5)) / (2 * a)
    x2 = (-b - (delta ** 0.5)) / (2 * a)
    print(f"Valor X1= {x1}, Valor X2= {x2}")
    return


bhaskara(a, b, c)
