nome = "Maria"
idade = 25
salario = 4650.37000

msg = "%s tem %d e ganha R$%.2f" % (nome, idade, salario)
print(msg)

msg2 = "[{:-^20s}] tem {} anos e ganha R${:.2f}". format(nome, idade, salario)
print(msg2)

msg3 = f"{nome:*^15s} tem {idade*100} anos e ganha R${salario:.2f}"
print(msg3)
