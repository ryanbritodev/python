fila = list()

while True:
    acao = input("Digite A para adicionar na fila e R para remover da fila: ")
    if acao == "A":
        nome = input("Digite o nome da pessoa: ")
        fila.append(nome)
    elif acao == "R":
        rem = fila.pop(0) # pop vazio sempre exclui o último elemento
        print(f"Remoção foi realizada!")
        if len(fila) == 1:
            print(f"O tamanho da fila agora é de 1 pessoa.")
        elif len(fila) > 1:
            print(f"O tamanho da fila agora é de {len(fila)} pessoas.")
    else:
        print("Comando inválido!")

    print(fila)
    encerrar = input("Deseja encerrar a fila? (Digite S para encerrar ou qualquer tecla pra continuar) ")

    if encerrar == "S":
        break

print(fila)
