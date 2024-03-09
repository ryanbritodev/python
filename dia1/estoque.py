print("ESTOQUE ANA BEATRIZ")

faixa = 7
melox = 5
dip = 6
micro = 3
palito = 15

while True:
    item_desejado = input("DIGITE O ITEM DO ESTOQUE QUE VOCÊ DESEJA SABER A QUANTIDADE (ou digite 'sair' para encerrar): ")

    if item_desejado.lower() == "sair":
        print("Programa encerrado.")
        break

    if item_desejado.lower() == "faixa de esparadrapo":
        print("Faixa de Esparadrapo: ", faixa, " unidades.")
    elif item_desejado.lower() == "meloxicam":
        print("Meloxicam: ", melox, "frascos")
    elif item_desejado.lower() == "dipirona":
        print("Dipirona: ", dip, "frascos")
    elif item_desejado.lower() == "microchip":
        print("Microchip: ", micro, "unidades")
    elif item_desejado.lower() == "palito de sorvete":
        print("Palitos de Sorvete: ", palito, "unidades")
    else:
        print("Item inválido, digite novamente:")
      
