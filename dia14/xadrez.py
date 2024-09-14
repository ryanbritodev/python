import matplotlib.pyplot as plt

def imprimirXadrez(linhas, colunas):
    bitBranco = [255, 255, 255]
    bitPreto = [0, 0, 0]
    linha = []
    chess = []
    if linhas != colunas:
        return None
    else:
        for i in range(linhas):
            linha = []
            if linhas % 2 == 0:
                for j in range(colunas // 2):
                    if linhas % 2 == 0:
                        if colunas % 2 == 0 and i % 2 != 0:
                            linha.append(bitPreto)
                            linha.append(bitBranco)
                        else:
                            linha.append(bitBranco)
                            linha.append(bitPreto)
            else:
                for j in range(colunas // 2):
                    if colunas % 2 != 0 and i % 2 != 0:
                        linha.append(bitPreto)
                        linha.append(bitBranco)
                    else:
                        linha.append(bitBranco)
                        linha.append(bitPreto)
            chess.append(linha)
        return chess


print(imprimirXadrez(8, 8))  # Depuração

# xadrez = [
#     [[255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0]],
#     [[0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255]],
#     [[255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0]],
#     [[0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255]],
#     [[255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0]],
#     [[0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255]],
#     [[255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0]],
#     [[0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255]]
# ]

plt.imshow(imprimirXadrez(8, 8))
plt.axis('off')
plt.show()
