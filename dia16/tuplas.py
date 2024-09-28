tuplas = 1, 2, True, ["Cássio", False, 2], "Olá"

# Convertendo
tuplas2 = tuple([1, 2, True, ["Cássio", False, 2], "Olá"])

# Tipo
print(type(tuplas))

print(tuplas2[2])

# Acessando
print(tuplas2[-1])

tupla1 = (1,2,3)

# Concatenação
tupla3 = tupla1 + tuplas2
print(tupla3)

for i in tupla3:
    print(i)
