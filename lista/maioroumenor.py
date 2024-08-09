print("PROGRAMA MAIOR OU MENOR")

while True:
    try:
        num1 = float(input("Digite o primeiro número: ").strip())
        num2 = float(input("Digite o segundo número: ").strip())
        break
    except ValueError:
        print("Erro! Por favor, insira um número válido: ")

if num1 > num2:
    print(f"{num1} é maior que {num2}!")
elif num2 > num1:
    print(f"{num2} é maior que {num1}!")
else:
    print(f"Os números são iguais!")
