import random
from sort_methods import sorter

lista = list(range(1, 50001))

random.shuffle(lista)

print(sorter.merge_sort(lista))
