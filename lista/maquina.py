# Exibe a tabela de códigos e preços explicitamente
print("Tabela de códigos e preços:")
print("Código | Preço (R$)")
print("------ | ---------")
print("  1    |  0.50")
print("  2    |  1.00")
print("  3    |  4.00")
print("  5    |  7.00")
print("  9    |  8.00")

# Preços para cada código
codigo_1 = 0.50
codigo_2 = 1.00
codigo_3 = 4.00
codigo_5 = 7.00
codigo_9 = 8.00

# Inicializa o total das compras
total_compras = 0

while True:
    try:
        # Solicita o código do produto
        codigo = int(input("Digite o código do produto (0 para finalizar): "))

        # Se o código for zero, quebra o loop
        if codigo == 0:
            break

        # Determina o preço com base no código
        if codigo == 1:
            preco = codigo_1
        elif codigo == 2:
            preco = codigo_2
        elif codigo == 3:
            preco = codigo_3
        elif codigo == 5:
            preco = codigo_5
        elif codigo == 9:
            preco = codigo_9
        else:
            # Código inválido
            print("Código inválido. Por favor, digite um código válido.")
            continue

        # Solicita a quantidade comprada
        quantidade = int(input("Digite a quantidade comprada: "))

        # Calcula o custo total para o produto
        custo_produto = preco * quantidade

        # Adiciona ao total geral
        total_compras += custo_produto

        # Exibe o subtotal
        print(f"Subtotal: R$ {total_compras:.2f}")

    except ValueError:
        # Se a entrada não for um número inteiro, exibe mensagem de erro
        print("Por favor, insira um número inteiro válido.")

# Exibe o total final das compras
print(f"Total das compras: R$ {total_compras:.2f}")
