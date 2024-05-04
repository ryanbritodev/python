lista1 = [1, 2, 3, 4, 5]
lista2 = ["M", "N", "I", 1, 2, 3, [4, 5]]

a = list("TEXTO")
print(a)
print(lista1[::2])
print(lista1[1::2])
print(lista1[0:3])
print(lista2[-7:-1])
print(lista1)
print(type(lista1))
print(lista2)
print(type(lista2))
print(lista1[0])
print(lista2[2])
print(type(lista2[3]))
print(len(lista1))
print(len(lista2))

lista1.pop(0)
var = lista1.pop(0)
print(var)
print(lista1, "METODO POP")

# Declarando listas:
# a = list()
# a = []

animais = []
print(animais)
a = input("Digite o seu bicho de estimação: ")
animais.append(a)
print(animais)
animais.append("gato")
print(animais)
lista3 = ["felinos", "aves"]
animais.extend(lista3[0])
# animais.append(["a", "b"])
animais.extend(["a", "b"])
print(animais)
print([1, 2] + [3, 4])

x = [1, 2, 3, 4, 5]
y = x
x[0] = 0
print(x)
print(y)
# Apenas aponta para lista, não copia ela
# Para copiar, devemos usar o método .copy
