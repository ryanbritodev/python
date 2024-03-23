print("CONVERSÃO DE DIAS, HORAS, MINUTOS E SEGUNDOS PARA SEGUNDOS")
dias = int(input("Insira a quantidade de dias: "))
horas = int(input("Insira a quantidade de horas: "))
minutos = int(input("Insira a quantidade de minutos: "))
segundos = int(input("Insira a quantidada de segundos: "))

diaEmSegundo = dias * 86400
horaEmSegundo = horas * 3600
minutoEmSegundo = minutos * 60

resultado = diaEmSegundo + horaEmSegundo + minutoEmSegundo + segundos

print("O valor convertido é de: ", resultado, "segundos.")
