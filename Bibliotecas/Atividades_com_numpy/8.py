import numpy as np

print("Insira os 9 elementos da matriz 3x3:")
elementos = []
for i in range(9):
    valor = float(input(f"Elemento {i+1}: "))
    elementos.append(valor)

# Converte a lista em uma matriz 3x3
matriz = np.array(elementos).reshape(3, 3)


print("\nMatriz 3x3 formatada:")
print(matriz)
