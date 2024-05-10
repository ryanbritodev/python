while True:
    while True:
        p1p =  input("Escolha P para PAR ou I para ÍMPAR: ")
        if p1p == "P" or p1p == "I":
            break

    if p1p == "P":
        p2p = "I"
    else:
        p2p = "P"

    p1 = int(input("Digite seu número (jogador 1): "))
    p2 = int(input("Digite seu número (jogador 2): "))
    soma = p1 + p2

    print(f"A soma dos números é {soma}")

    if soma % 2 == 0:
        resultado = "P"
        print("O resultado é par")
    else:
        resultado = "I"
        print("O resultado é ímpar")

    if p1p == resultado:
        print("O jogador 1 é o vencedor")
    else:
        print("O jogador 2 é o vencedor")

    cod = input("Digite SAIR para sair ou qualquer tecla para continuar: ")
    if cod == "SAIR":
        break
