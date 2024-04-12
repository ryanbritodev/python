import sys

print("CALCULE SEU GASTO DE ENERGIA ELÉTRICA")
energiaGasta = float(input("Qual a quantidade de kWh consumida na sua instalação? "))
print("R PARA RESIDENCIAL | C PARA COMERCIAL | I PARA INDUSTRIAL")
instalacao = input("Qual o tipo da sua instalação? ")

if instalacao == "R" and energiaGasta <= 500:
    valor = energiaGasta * 0.40
elif instalacao == "R" and energiaGasta > 500:
    valor = energiaGasta * 0.65
elif instalacao == "C" and energiaGasta <= 1000:
    valor = energiaGasta * 0.55
elif instalacao == "C" and energiaGasta > 1000:
    valor = energiaGasta * 0.60
elif instalacao == "I" and energiaGasta <= 5000:
    valor = energiaGasta * 0.55
elif instalacao == "I" and energiaGasta > 5000:
    valor = energiaGasta * 0.60
else:
    sys.exit("ERRO! RESPOSTA INVÁLIDA")

if instalacao == "R":
    print(f"O valor da energia elétrica que você deve pagar, já que sua instalação é do tipo residencial, é de aproximadamente R${valor}")
elif instalacao == "C":
    print(f"O valor da energia elétrica que você deve pagar, já que sua instalação é do tipo comercial, é de aproximadamente R${valor}")
elif instalacao == "I":
    print(f"O valor da energia elétrica que você deve pagar, já que sua instalação é do tipo industrial, é de aproximadamente R${valor}")
