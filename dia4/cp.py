print(50*"*")
print("     Olá! Seja muito bem-vindo a Frutaria ES!     ")
print(50*"*")

nome = input("Para começarmos, por favor, informe seu nome: ")
endereco = input(f"{nome}, diga o seu endereço: ")
ano = int(input(f"{nome}, diga o ano de nascimento: "))
idade = 2024 - ano

mensagem = """
 -------------------------------
 FRUTA                     R$/kg
 -------------------------------
 Banana                    10.50
 Uva                       3.50 
 Maçã                      8.50 
 Melancia                  20.50
 Kiwi                      35.40
 -------------------------------
"""

print("As opções de fruta do dia são: ")
print(mensagem)

fruta = input("Escolha a fruta que você deseja: ")
peso = float(input("Qual é a quantidade (em kg) que você deseja? "))

if fruta == "banana":
    valor = peso * 10.50
elif fruta == "uva":
    valor = peso * 3.50
elif fruta == "maçã":
    valor = peso * 8.50
elif fruta == "melancia":
    valor = peso * 20.50
elif fruta == "kiwi":
    valor = peso * 35.40
else:
    print("Escolha inválida!")
    exit()

frete = 4

if valor < 15:
    valor = valor + frete
else:
    print(f"{nome}, você está isento de frete!")

if idade > 60:
    print(f"{nome}, o (a) Sr(a) tem um desconto de 5%.")
    valor = valor * 0.95

print(f"Muito obrigado {nome}, sua compra ficou no valor de R${valor:.2f} e será entregue no endereço: {endereco}")
