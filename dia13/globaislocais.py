# Variáveis Locais são somente visíveis para aquela função
# Variáveis globais são visíveis para todas
# Visualização de Lógica de Códigos em Python
# https://pythontutor.com/render.html#mode=display
# Fluxogramas em Python do nosso código
# draw.io

def f1(a):
    x = 10
    print(a + x)


def f2(a):
    c = 10
    print(a + x + c)


x = 4

f1(3)
f2(2)

print(x)