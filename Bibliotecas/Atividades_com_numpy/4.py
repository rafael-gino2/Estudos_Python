
# 4. Ler uma matriz D 5 x 5 (considere que não serão informados valores duplicados). A
# seguir ler um número X e escreva uma mensagem indicando se o valor de X existe ou
# NÃO na matriz.
import numpy as np
matriz = np.arange(1,26).reshape(5,5)
num_escolhido = int(input('Insira seu número: '))

if num_escolhido in matriz:
    print('O numero escolhido existe na matriz')
else:
    print('O numero escolhido não existe na matriz')
print(matriz)