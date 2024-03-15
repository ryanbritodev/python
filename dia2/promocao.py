print("CALCULADORA DE PORCENTAGEM DE AUMENTO EM UMA PROMOÇÃO DE CARGO")

salario = int(input("Qual o seu salário? "))
aumento = int(input("Qual foi a porcentagem de aumento do seu salário? "))

promocao = salario * (aumento / 100)
novoSalario = int(salario + promocao)

print("Parabéns! Seu sálario inicial era de R$", salario, "porém com sua promoção, seu novo salário é de R$", novoSalario)
