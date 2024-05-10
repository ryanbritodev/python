print("TABUADA DE ADIÇÃO, SUBTRAÇÃO, DIVISÃO E MULTIPLICAÇÃO")

# Validar entrada do número e operador
while True:
    try:
        numero = int(input("Digite o número que você deseja saber a tabuada: "))
        operador = input("Digite o operador que você deseja (x, -, +, /): ").lower()
        if operador in ["x", "-", "+", "/"]:
            break
        else:
            print("Operador inválido. Tente novamente.")
    except ValueError:
        print("Erro! Por favor, insira um número válido.")

numero2 = 1
print(f"TABUADA DO {numero}")

# Loop contínuo para tabuada
while True:
    if operador == "x":
        print(f"{numero} x {numero2} = {numero * numero2}")
    elif operador == "+":
        print(f"{numero} + {numero2} = {numero + numero2}")
    elif operador == "-":
        print(f"{numero} - {numero2} = {numero - numero2}")
    elif operador == "/":
        if numero2 != 0:
            print(f"{numero} / {numero2} = {numero / numero2:.2f}")
        else:
            print("Divisão por zero não é permitida.")

    while True:
        sair = input("DESEJA CONTINUAR? (s/n): ").lower()
        if sair in ["s", "n"]:
            break
        else:
            print("Resposta inválida! Por favor, digite 's' para continuar ou 'n' para encerrar.")

    if sair == "n":
        print("TABUADA ENCERRADA")
        break

    numero2 += 1
