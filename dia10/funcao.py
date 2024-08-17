from math import pow

valor = float(input("Vamos calcular uma função matemática? "))

def y(x):
    if x <= 2:
        return x
    elif x <= 3.5:
        return 2
    elif x < 5:
        return 3
    else:
        return int(pow(x, 2)) - 10 * x + 28

print(y(valor))

# Uma função é definida da seguinte forma:
# def nome(parâmetro1, parâmetro2, ..., parâmetro3):
#   comandos
#   return valor do retorno
# Os parâmetros são variáveis, que são inicialização com valores
# indicados durante a chamada/invocação da função
# O comando return devolve para o invocador da função o resultado de execução desta
