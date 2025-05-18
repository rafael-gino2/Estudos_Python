import numpy as np

print("Insira os 4 elementos da primeira matriz 2x2:")
matriz1 = []
for i in range(4):
    valor = float(input(f"Matriz 1 - Elemento {i+1}: "))
    matriz1.append(valor)
matriz1 = np.array(matriz1).reshape(2, 2)

print("Insira os 4 elementos da segunda matriz 2x2:")
matriz2 = []
for i in range(4):
    valor = float(input(f"Matriz 2 - Elemento {i+1}: "))
    matriz2.append(valor)
matriz2 = np.array(matriz2).reshape(2, 2)


matriz_soma = matriz1 + matriz2

print("\nResultado da soma das duas matrizes 2x2:")
print(matriz_soma)
