# Faça um programa que dado o nome de uma pessoa, escreve na tela o número de letras do nome e a primeira letra do nome

nome = input("Qual o seu nome? ") + ","
tamanho = len(nome)
primeiraLetra = nome[0] + "."

print(nome, "o seu nome possui", tamanho, "letras e a primeira letra do seu nome é", primeiraLetra)
