# 2. Ler 2 matrizes, A 4 x 6 e B 4 x 6 e criar:
# a) uma matriz S que seja a soma de A e B.
# b) uma matriz D que seja a diferença de A e B. (A – B).
# Escrever as matrizes S e D após todo cálculo estar concluído.
import numpy as np
matriz = np.random.randint(1, 10, (4, 6))
matriz2 = np.random.randint(1, 10, (4, 6))
matrizS = matriz + matriz2
matrizD = matriz - matriz2
print('Matriz S: ')
print(f'{matrizS}')
print('Matriz D: ')
print(f'{matrizD}')