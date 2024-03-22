# Escreva um programa que retorne se o cliente pode ou não contratar um empréstimo (com basa na idade e salárip)
salario = int(input("Qual o seu salário? "))
idade = int(input("Qual a sua idade? "))
mamatinha = input("Você tem alguma condição especial? Responda com S ou N ")

s = salario >= 1500
i = idade >= 18
resposta = "S"

print(s and i or mamatinha == resposta)
