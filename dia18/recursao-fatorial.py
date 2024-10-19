valor = 5


def fatorial(numero):
    if numero == 1:
        return numero
    return numero * fatorial(numero - 1)


print(fatorial(valor))
