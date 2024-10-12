lista_de_compras = "biscoito", "chocolate", "farinha", "ovo"

supermercado = {
    "amaciante": 4.99,
    "arroz": 10.90,
    "biscoito": 1.69,
    "chocolate": 3.99,
    "farinha": 2.99
}


def compras(lista, market):
    valor = 0
    temNoSup = []
    nTemNoSup = []
    # Percorrendo a lista de compras
    for item in lista:
        if item in market:
            valor += market[item]
            temNoSup.append(item)
        else:
            nTemNoSup.append(item)
    return valor, temNoSup, nTemNoSup


print(compras(lista_de_compras, supermercado))
