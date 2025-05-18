
# 3. Ler uma matriz A de 4 x 4, calcular e escrever as somas dos elementos marcados com o
# X. Utilizar estruturas de repetição.
# X X - -
# X X - -
# - - - -
# - - - -

# - - - -
# - - - -
# - - X X
# - - X X

# X - -
# X X - -
# X X X -
# X X X X

# - X X X
# - - X X
# - - - X
# - - - -
import numpy as np
A = np.random.randint(1, 10, (4, 4))

# Exibir a matriz A
print("Matriz A:")
print(A)

# Função para calcular e somar os elementos marcados com "X" no padrão 1
def soma_padrao_1(matriz):
    soma = 0
    # X X - -,
    # X X - -,
    # - - - -,
    # - - - -
    for linha in range(2):  # Linhas 0 e 1
        for coluna in range(2):  # Colunas 0 e 1
            soma += matriz[linha, coluna]
    return soma

# Função para calcular e somar os elementos marcados com "X" no padrão 2
def soma_padrao_2(matriz):
    soma = 0
    # - - - -,
    # - - - -,
    # - - X X,
    # - - X X
    for linha in range(2, 4):  # Linhas 2 e 3
        for coluna in range(2, 4):  # Colunas 2 e 3
            soma += matriz[linha, coluna]
    return soma

# Função para calcular e somar os elementos marcados com "X" no padrão 3
def soma_padrao_3(matriz):
    soma = 0
    # X - - -,
    # X X - -,
    # X X X -,
    # X X X X
    for linha in range(4):  # Todas as linhas
        for coluna in range(linha + 1):  # Colunas da diagonal e abaixo
            soma += matriz[linha, coluna]
    return soma

# Função para calcular e somar os elementos marcados com "X" no padrão 4
def soma_padrao_4(matriz):
    soma = 0
    # Padrão 4: - X X X, - - X X, - - - X, - - - -
    for i in range(4):  # Todas as linhas
        for j in range(4 - i - 1, 4):  # Colunas variando conforme linha
            soma += matriz[i, j]
    return soma

# Calcular e exibir a soma para cada padrão
soma_1 = soma_padrao_1(A)
soma_2 = soma_padrao_2(A)
soma_3 = soma_padrao_3(A)
soma_4 = soma_padrao_4(A)

# Exibir resultados
print(f"Soma dos elementos marcados com X no Padrão 1: {soma_1}")
print(f"Soma dos elementos marcados com X no Padrão 2: {soma_2}")
print(f"Soma dos elementos marcados com X no Padrão 3: {soma_3}")
print(f"Soma dos elementos marcados com X no Padrão 4: {soma_4}")