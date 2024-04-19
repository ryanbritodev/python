import time

tempo = 10

while tempo > 0:
    print(tempo)
    tempo = tempo - 1
    time.sleep(1)
    if tempo == 0:
        print("Fogo!")
