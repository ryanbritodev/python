# RECURSÃO POTÊNCIA

def pot(numero, potencia):
    if potencia == 0:
        return 1
    elif potencia == 1:
        return numero
    return numero * pot(numero, potencia - 1)


print(pot(5, 5))
