from time import sleep

# ALGORITMOS
# Finitude (deve ter um fim após um número de passos),
# bem-definido (deve ter um caminho bem encorpado), entradas, saídas,
# efetividade (todas as operações devem ser eficazes, e não infinitas

# JUPYTER NOTEBOOK - NEW FILE VS CODE
# IDE - Pychar, VSCode, Google Colab, Sypder, IDLE
# Executar programas, editar, depurar

# Operador relacional sempre retorna variável booleana
# Operador lógico not and ou or
# Aritméticos, relacionais e lógicos (ordem)

num = int(input("Digite o número de linhas para sua árvore: "))
estrelas = "■"

print(f"{'★':^{num * 2 - 1}}")
for i in range(1, num + 1):
    print(f"{estrelas:^{num * 2 - 1}}")
    sleep(0.1)
    estrelas = estrelas + "■■"
print(f"\n{'FELIZ NATAL!':^{num * 2 - 1}}")
