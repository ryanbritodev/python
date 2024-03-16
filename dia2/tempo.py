print("CONVERSÃO DE SEGUNDOS EM MESES, SEMANAS, DIAS, HORAS, MINUTOS E SEGUNDOS")

tempo = int(input("Insira a quantidade de segundos: "))
meses = int(tempo // 2.628e+6)
semanas = tempo // 604800
dias = tempo // 86400
horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60

print(f"Essa quantidade de segundos representa {meses} mês(es), {semanas} semana(s), {dias} dia(s), {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s).")
