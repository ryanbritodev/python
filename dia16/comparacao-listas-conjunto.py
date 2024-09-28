a = [1, 3, 4, 8, 7, 7]
b = [3, 9, 2, 4, 1, 1, 5]

valoresComum = set(a) & set(b)

print(valoresComum)

valoresPrimeira = set(a) - set(b)
valoresSegunda = set(b) - set(a)
print()

print(valoresPrimeira)
print()

print(valoresSegunda)

valoresNaoRepetidos = set(a) | set(b)

print()
print(valoresNaoRepetidos)
