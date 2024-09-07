# Lista com 10 termos 1 usando List Comprehension
list = [1 for i in range(10)]
print(list)

list = [i*2 for i in range(10)]
print(list)

for i in range(10):
    print(i)

# Faça uma lista que contenha os múltiplos de 3 até 100
listinha = [i for i in range(100) if i % 3 == 0]
# ou
# listinha = [i for i in range(0, 101) if i * 3 <= 100]
print(listinha)

print()

colunas = 3
matriz = lambda linhas, colunas: [[int(input("Insira o valor: ")) for i in range(colunas)] for j in range(linhas)]
print(matriz(2, 3))
