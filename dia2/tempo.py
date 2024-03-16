print("CONVERSÃO DE SEGUNDOS EM DIAS, HORAS, MINUTOS E SEGUNDOS")

tempo = int(input("Insira a quantidade de segundos: "))
dias = tempo // 86400
horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60

print(f"Essa quantidade de segundos representa {dias} dia(s), {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s).")
