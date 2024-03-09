# Exercício: Escreva um programa que calcule as raízes de uma de uma equação de segundo grau: ax^2 + bx + c = 0

print("Quais as raízes quadradas dessa equação de segundo grau: X^2 - 3X - 10 = 0?")

a = 1
b = -3
c = -10

delta = (b ** 2) - 4 * a * c

x1 = (-b + (delta ** 0.5)) / 2 * a
x2 = (-b - (delta ** 0.5)) / 2 * a

# Para realizar uma raíz quadrada podemos utilizar o operador **, elevando o número à potência 1/2 (0.5)

print("As raízes quadradas dessa equação são:")
print(x1)
print(x2)
