while True:
    try:
        escolha = input("Digite o código da fruta desejada (ou 0 para sair): ")
        if escolha == "0":
            print("Saindo do programa...")
            break

        kilo = float(input("Digite o peso desejado em quilos: "))
        valor = 0

        if escolha == "1":
            valor += 12.90 * kilo
        elif escolha == "2":
            valor += 9.30 * kilo
        elif escolha == "3":
            valor += 3.50 * kilo
        elif escolha == "4":
            valor += 7.00 * kilo
        elif escolha == "5":
            valor += 37.50 * kilo
        else:
            print("Código Inválido")
            continue

    except ValueError:
        print("Erro! Certifique-se de digitar um número válido para o peso.")
        continue

print(f"O valor total da compra é R${valor:.2f}")
