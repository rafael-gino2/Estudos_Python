# ATIVIDADE 36
# 6. Ler uma matriz A 12 x 13 e divida todos os 13 elementos de cada uma das 12 linhas de
# A pelo valor do maior elemento daquela linha. Escrever a matriz A modificada.
import numpy as np

# Criando a matriz 12x13 com valores de 1 a 156
matriz = np.arange(1, 157).reshape(12, 13)

# Lista para armazenar a matriz modificada
divisao = []

# Percorre cada linha da matriz
for linha in matriz:
    maior_num = max(linha)  # Obtém o maior número da linha atual
    divisao_num = linha / maior_num  # Divide todos os elementos da linha pelo maior número
    divisao.append(divisao_num)  # Adiciona a linha modificada à lista

# Convertendo a lista para um array NumPy para exibição organizada
matriz_modificada = np.array(divisao)

# Exibindo a matriz original
print("Matriz original:")
print(matriz)

# Exibindo a matriz modificada
print("\nMatriz modificada (cada linha dividida pelo maior valor da linha):")
print(matriz_modificada)
