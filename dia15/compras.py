supermercado = {
    'amaciante': 4.99,
    'arroz': 10.90,
    'biscoito': 1.69,
    'cafe': 6.98,
    'chocolate': 3.79,
    'farinha': 2.99
}


def listaDeCompras(*args):
    soma = 0
    for produto in supermercado.keys():
        for argumento in args:
            if produto == argumento:
                soma += supermercado[produto]
            else:
                continue
    return soma


print(listaDeCompras("amaciante", "arroz"))
