# valor = 3
# pi = 1 - 1 / valor
#
# for i in range(0, 100000):
#     pi += 1 / valor
#     valor += 2
#     pi -= 1 / valor
#     print(pi*4)

quantidade = 100000000
pi = 0

for i in range(quantidade):
    termo = (-1) ** i/(2*i+1)
    # print(f"{(-1)**i}/{2*i+1}")
    pi += 4 * termo
print(pi)

# Nesse programa calculamos a constante de leibniz, que visa calcular a 