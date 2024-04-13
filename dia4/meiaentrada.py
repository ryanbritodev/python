import sys

print("SAIBA SE VOCÊ TEM DIREITO A MEIA ENTRADA")

idade = int(input("Qual sua idade? "))
if idade > 65 or idade < 21:
    print("Você tem direito a meia entrada!")
    exit()

estudante = input("Você é estudante? (S ou N) ")
if estudante == "S":
    print("Você tem direito a meia entrada!")
elif estudante == "N":
    print("Você não tem direito a meia-entrada!")
else:
    sys.exit("RESPOSTA INVÁLIDA")
