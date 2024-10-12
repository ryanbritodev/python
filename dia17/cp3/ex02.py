a = [("Equipe A", 90), ("Equipe B", 40), ("Equipe C", 95), ("Equipe D", 120), ("Equipe E", 105)]


def ordena(a):
    for iter in range(len(a) - 1, 0, -1):
        for i in range(iter):
            if a[i][1] > a[i + 1][1]:
                aux = a[i]
                a[i] = a[i + 1]
                a[i + 1] = aux


ordena(a)
print(a)
