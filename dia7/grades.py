quantidade = int(input("Digite a quantidade de notas você deseja realizar a média: "))
listaNotas = []
balde = 0

for i in range(quantidade):
    nota = float(input(f"Digite a nota {i +1}: "))
    listaNotas.append(nota)
    balde += nota

print(f"A soma das notas é {balde}")
print(f"A média das notas é {(balde / quantidade):.2f}")
