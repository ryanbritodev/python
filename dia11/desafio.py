from soma import soma
from subtracao import subtracao
from calculos import divisao, multiplicacao

# Faça um programa calculadora no programa principal que chame
# as funções de soma, subtração, multiplicação e divisão na fórmula de módulo
# junte duas operações no mesmo módulo

calculadora = """CALCULADORA
+ ...... 1
- ...... 2
/ ...... 3
* ...... 4"""

while True:
    num1 = float(input("Digite o 1° número: "))
    num2 = float(input("Digite o 2° número: "))
    print(calculadora)
    operador = int(input("ESCOLHA O SEU OPERADOR ou 0 para sair: "))
    while operador != 1 and operador != 2 and operador != 3 and operador != 4:
        print("Resposta inválida!")
        operador = int(input("ESCOLHA O SEU OPERADOR ou 0 para sair: "))
    if operador == 1:
        print(soma(num1, num2))
    elif operador == 2:
        print(subtracao(num1, num2))
    elif operador == 3:
        print(divisao(num1, num2))
    elif operador == 4:
        print(multiplicacao(num1, num2))
    flag = str(input("Calcular novo número? [S/N] ")).strip().upper()[0]
    if flag == "S":
        continue
    else:
        print("Compreensível! Tenha um bom dia")
        break
