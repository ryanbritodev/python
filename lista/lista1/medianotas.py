print("CALCULADORA DE MÉDIA DE NOTAS")

while True:
    try:
        quantidadeNotas = int(input("Digite o número de notas a serem calculadas: ").strip())
        break
    except ValueError:
        print("Número inválido! Tente novamente: ")

i = 1
notaMedia = 0

while i <= quantidadeNotas:
    try:
        valorNota = float(input(f"Digite a {i}º nota: ").strip())
        notaMedia += valorNota
        i += 1
    except ValueError:
        print("Número inválido! Tente novamente: ")

nota = notaMedia / quantidadeNotas
notaFormatada = "{:.2f}".format(nota)

print(f"A média das notas será de aproximadamente {notaFormatada}")
