# Exercício: Escreva um programa que calcule as raízes de uma de uma equação de segundo grau

print("CALCULADORA DE RAIZ DE EQUAÇÃO DE SEGUNDO GRAU")

a = int(input("Coloque um valor para a: "))
b = int(input("Coloque um valor para b: "))
c = int(input("Coloque um valor para c: "))

delta = (b ** 2) - 4 * a * c

x1 = (-b + (delta ** 0.5)) / (2 * a)
x2 = (-b - (delta ** 0.5)) / (2 * a)

# Para realizar uma raíz quadrada podemos utilizar o operador **, elevando o número à potência 1/2 (0.5)

print("As raízes quadradas dessa equação são:")
print("X1 =", x1)
print("X2 =", x2)
