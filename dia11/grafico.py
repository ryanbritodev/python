import matplotlib.pyplot as plt
from funcaozinha import y

x = []

for i in range(101):
    x.append(i*6/100)

yy = []

for i in x:
    y(i)
    yy.append(y(i))

plt.plot(x, yy, marker="", linestyle="dotted")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Gráfico")
plt.grid(True)
plt.show()
