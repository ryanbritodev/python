from time import sleep

print("RELÓGIO 24 HORAS")

for horas in range(24):
    for minutos in range(60):
        for segundos in range(60):
            for milisegundos in range(100):
                print(f"{horas:02d}:{minutos:02d}:{segundos:02d}:{milisegundos:03d}")
                sleep(0.01)
