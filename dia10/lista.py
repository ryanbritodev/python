notas = [1, 2, 3.1, "Maria", True, [1, 2]]
for i in notas:
    print(i, type(i))
print(type(notas))
print(len(notas))
print(notas[1:6])
print(notas[::-1])

lista = notas
print(notas)
print(lista)
notas[0] = 250
print(notas)
print(lista)
# Lista funciona como ponteiro, se alteramos algo, ela muda tudo
lista = notas.copy()
# Método para copiar uma lista
# lista = notas[:]
# ^^^ MESMA COISA
print(notas[-1][0])
# ACESSANDO UMA LISTA DENTRO DE UMA LISTA
# APPEND SEMPRE ADICIONA AO FINAL DA LISTA

