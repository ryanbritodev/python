import builtins

a = [
    [1, 2, 3],
    [5, 8, 10]
]

b = []

for j in range(len(a[0])):
    linha = []
    for i in range(len(a)):
        linha.append(a[i][j])
        # print(a[j][i])
    b.append(linha)
print(a)
print(b)
