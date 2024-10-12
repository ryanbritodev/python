lista = [3, 1, 2, 50, 100, 10, 134, 23, 12, 9, 8, 7, 6, 4]


def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]


selection_sort(lista)
print(lista)
