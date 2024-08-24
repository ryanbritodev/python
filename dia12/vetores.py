from random import randint

n1 = []
n2 = []
mult = []
indice = 0

for i in range(0, 101):
    random = randint(1, 100)
    random2 = randint(1, 100)
    n1.append(random)
    n2.append(random2)

total = 0

for valores in n1:
    mult.append(valores * n2[indice])
    total += mult[indice]
    indice += 1

print("Primeira lista: ", n1)
print("Segunda lista: ", n2)
print("Multiplicação entres as listas: ", mult)
print("Soma total:", total)


def prodint(v, w, z):
    if len(v) != len(w):
        return "Valor inválido!"
    soma = 0
    for i in range(len(v)):
        termo = v[i] * w[i] / z[i]
        soma += termo
    return soma


#print("Soma função:", prodint(n1, n2))

quantidade = 10
lista1 = []
for i in range(quantidade):
    lista1.append(1)
print(lista1)

lista2 = []
for i in range(quantidade):
    lista2.append((-1) ** i)
print(lista2)

lista3 = []
for i in range(quantidade):
    lista3.append(2*i+1)
print(lista3)

print(4*prodint(lista1, lista2, lista3))
