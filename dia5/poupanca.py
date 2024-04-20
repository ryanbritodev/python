deposito = float(input("Digite o valor do seu depósito inicial: "))
taxa = float(input("Digite o valor da taxa de juros mensal: "))
depositoMensal = float(input("Digite o valor do depósito mensal: "))
periodo = int(input("Digite o período (em meses): "))

mes = 1

while mes <= periodo:
    deposito = deposito + depositoMensal
    montante = deposito * (1 + taxa / 100) ** mes
    print(f"O valor da poupança no mês {mes} foi: {montante:.2f}")
    mes += 1
