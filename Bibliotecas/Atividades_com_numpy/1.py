#ATIVIDADE 1
# Ler uma matriz M 5 x 5, calcular e escrever as seguintes somas:
# a) da linha 3 de M
# b) da coluna 2 de M
# c) da diagonal principal
# d) da diagonal secundária
# e) de todos os elementos da matriz
# Obs: Na figura abaixo o X indica os elementos que devem ser somados
# Linha 3
# - - - - -
# - - - - -
# - - - - -
# X X X X X
# - - - - -

# Coluna 2
# - - X - -
# - - X - -
# - - X - -
# - - X - -
# - - X - -
# Diagonal Principal
# X - - - -
# - X - - -
# - - X - -
# - - - X -
# - - - - X

# Diagonal Secundária
# - - - - X
# - - - X -
# - - X - -
# - X - - -
# X - - - -
# Todos os elementos
# X X X X X
# X X X X X
# X X X X X
# X X X X X
# X X X X X


import numpy as np
# O ramdom.randit(1,10) vai gerar numeros aleatorios de 1 a 9 para a matriz que dps é definida como 5x5
matriz = np.random.randint(1, 10, (5, 5))
print(f'{matriz}')

# Aq eu to criando uma variavel da soma q guarda a matriz e soma a fileira q escolhermos da matriz q é a 3 (O python começa contando do 0)
soma_linha_3 = matriz[3, :].sum()
print(f"Soma da linha 3: {soma_linha_3}")

# Aq eu to criando uma variavel da soma q guarda a matriz e soma a coluna q escolhermos da matriz q nesse caso é a coluna 3 mas q na vdd é a 2 (O python começa contando do 0).
soma_coluna_2 = matriz[:, 2].sum()
print(f"Soma da coluna 2: {soma_coluna_2}")

# Aq eu fiz uma variavel para somar a diagonal da matriz usando o 'diagonal' do np e o sum para somar a diagonal.
soma_diagonal = np.diagonal(matriz).sum()
print(f'Soma da diagonal principal: {soma_diagonal}')

# Aq eu fiz uma variavel para somar a diagonal da matriz usando o 'diagonal' do np e o sum para somar a diagonal (msm coisa só que ao contrario). o fliplr serve para inverter os elementos.
soma_diagonal_contrario = np.diagonal(np.fliplr(matriz)).sum()
print(f'Soma da diagonal secundaria: {soma_diagonal_contrario}')

# Aq criei a variavel para somar td
soma_matriz = np.sum(matriz)
print(f'Soma dos elementos da matriz: {soma_matriz}')

