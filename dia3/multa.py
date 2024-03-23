velocidade = int(input("Qual era velocidade do seu veículo (em km/h) no momento em que você passou no radar? "))
multa = (velocidade - 80) * 5
if velocidade > 80:
    print("Que pena! Seu carro foi multado no valor de R$", multa)
if velocidade <= 80:
    print("Ufa! Você não foi multado.")
