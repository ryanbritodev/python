# Recursão de Soma
# Chamamos a função dentro dela mesma e colocamos o caso de saída, que satisfaça ela, antes da sua próxima chamada

lista = [1, 3, 5, 7, 9]


def soma(lista):
    if len(lista) == 1:
        return lista[0]
    # (Opcional) else:
    return lista[0] + soma(lista[1:])


# 1° caso:
# 1 + soma([3, 5, 6, 7, 9])
# 1 +

# 2° caso:
# 3 + soma([5, 7, 9])
# 3 +

# 3° caso:
# 5 + soma([7, 9])
# 5 +

# 4° caso:
# 7 + soma([9])     (Índice 0)
# 7 + 9

print(soma(lista))
