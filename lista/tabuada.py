print("TABUADA")
print("PROGRAMA PARA EXIBIR OS RESULTADOS DA TABUADA DE UM NÚMERO")

while True:
    try:
        numero = int(input("Digite o número que você deseja saber a tabuada: "))
        break
    except ValueError:
        print("Erro! Número inválido. Por favor, digite novamente: ")

i = 1
multiplicador = 1

print(f"TABUADA DO {numero}")

while i <= numero and 10 >= multiplicador:
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
    multiplicador += 1
