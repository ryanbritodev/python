print("SOMA DOS PARES")
print("SOME TODOS OS NÚMEROS PARES DENTRO DE UM INTERVALO NUMÉRICO")

while True:
    try:
        numero = int(input("Digite o número desejado: ").strip())
        break
    except ValueError:
        print("Número inválido! Tente novamente: ")

i = 0
soma = 0

while i <= numero:
    soma += i
    i += 2

""" 
EXEMPLO DE COMO FUNCIONA A REPETIÇÃO:
Primeira soma: i = 0, a soma é 0 + 0 = 0.
Segunda soma: i = 2, a soma é 0 + 2 = 2.
Terceira soma: i = 4, a soma é 2 + 4 = 6.
Quarta soma: i = 6, a soma é 6 + 6 = 12. 
"""

print(f"A soma de todos os números pares no intervalo é {soma}")
