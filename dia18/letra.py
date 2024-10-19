# Faça um programa que altera um texto de um arquivo substituindo a letra "a" por "A"

arquivo = open("letra.txt", "r+", encoding="UTF-8")

texto = arquivo.read()
arquivo.seek(0, 0)

textoNovo = ""
for i in texto:
    if i == "a":
        textoNovo += "A"
    else:
        textoNovo += i

arquivo.write(textoNovo)

arquivo.close()
