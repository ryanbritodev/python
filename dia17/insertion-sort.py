lista = [10, 41, 12, 98, 68, 56]


def insertion_sort(listinha):
    for i in range(1, len(listinha)):
        valor = listinha[i]
        j = i - 1
        while j >= 0 and valor < listinha[j]:
            listinha[j + 1] = listinha[j]
            j -= 1
        listinha[j + 1] = valor


insertion_sort(lista)
print(lista)
