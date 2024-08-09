print("PROGRAMA QUE LÊ NÚMEROS INTEIROS DO TECLADO")

# Variáveis para manter a soma, a quantidade de números e o número atual
soma = 0
quantidade = 0

while True:
    try:
        # Tenta ler um número do teclado
        numero = int(input("Digite um número inteiro (0 para parar): "))

        # Se o número for zero, quebra o loop
        if numero == 0:
            break

        # Adiciona o número à soma e incrementa a quantidade
        soma += numero
        quantidade += 1

    except ValueError:
        # Se o usuário digitar algo que não é um número inteiro, exibe uma mensagem de erro
        print("Por favor, insira um número inteiro válido.")

# Calcula a média aritmética se houver números para dividir
media = soma / quantidade if quantidade > 0 else 0

# Exibe a quantidade, soma e média
print("Quantidade de números digitados:", quantidade)
print("Soma dos números:", soma)
print("Média aritmética:", media)
