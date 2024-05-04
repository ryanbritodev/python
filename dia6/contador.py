from time import sleep

lista = list(range(0, 11))
lista.reverse()

for i in lista:
    print(i)
    sleep(1)
    if i == 0:
        print("BOOM!")
