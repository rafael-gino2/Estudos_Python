# 5. Ler uma matriz G 5 x 5 e criar 2 vetores SL e SC de 5 elementos que contenham
# respectivamente as somas das linhas e das colunas de G. Escrever os vetores criados.
import numpy as np

matriz2 = np.arange(1,26).reshape(5,5)
soma = 0
print(matriz2)
def coluna(soma):
   for coluna in matriz2:
     soma+=coluna
   return (f'Soma de cada coluna (SC): {soma}')

def linha(soma):
   soma_linhas = []
   for linha in matriz2:
     soma_linhas.append(int(sum(linha)))#Coloco int para o numpy reconhecer q é numero, e o soma linha ta pegando (apendando) a soma de cada linha que o for ta iterando da matriz2
   return (f'Soma de cada linha (SL): {soma_linhas}')

print(coluna(soma))
print(linha(soma))
