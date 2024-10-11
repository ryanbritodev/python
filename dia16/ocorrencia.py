# Exercício 1: Contar Ocorrências Crie uma função que recebe uma lista de palavras e retorna um dicionário com a contagem de cada palavra.

produtos = ['maçã', 'banana', 'maçã', 'laranja', 'banana', 'maçã']


def contar_ocorrencia(lista):
    dicionario = dict()
    for i in lista:
        valores = lista.count(i)
        if i in dicionario:
            continue
        else:
            dicionario[i] = valores

    return dicionario


print(contar_ocorrencia(produtos))
