frase = str(input("Escreva uma frase: "))
caracteres = dict()

for caractere in frase:
    chave = frase.count(caractere)
    if caractere in caracteres:
        continue
    else:
        caracteres[caractere] = chave

print(caracteres)
