# Modos de Abertura de Arquivo de Texto
# Sintaxe:
# arquivo = open("aula.txt", "modo")
# r = leitura
# w = escrita, apaga o conteudo que ja exisitr
# a = escrita, mas preserva o conteúdo se já existir
# b = modo binário
# + = atualização (leitura e escrita)

arquivo = open('arquivo.txt', 'r', encoding='UTF-8')
print(arquivo)
print(type(arquivo))

# Lenda bytes (caracteres)
# txt = arquivo.read(3)
# print(txt)

txt2 = arquivo.read()
print(txt2)

# readline = le uma linha inteira
# readlines = retorna uma lista com TODAS as linhas do arquivo

# seek = move o cursor
# 0 = inicio

txt3 = arquivo.read()
print(txt3)

arquivo.seek(0, 0)
txt4 = arquivo.read()
print(txt4)
