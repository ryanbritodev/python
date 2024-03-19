# Exercício: Faça um programa que avalie a sua nota e lhe retorne verdadeiro ou falso sobre sua aprovação na disciplina

n1 = int(input("Digite sua nota do primeiro trimestre: "))
n2 = int(input("Digie sua nota do segundo trimestre: "))
n3 = int(input("Digite sua nota do terceiro trimestre: "))

nota = n1 + n2 + n3

media = nota / 3

print(media >= 7)
