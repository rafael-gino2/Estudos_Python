# 7. Logo após, ler uma matriz 13 x 3 que contenha a aposta de um jogador. Considere que
# cada posição da matriz armazenará o valor 1 se for apostado, 0 caso contrário. Calcular
# e escrever o número de pontos obtidos pelo jogador. Escrever também o número de
# apostas simples, dupla ou tripla utilizadas pelo apostador.
import numpy as np

matriz = np.arange(1, 40).reshape(13, 3)

# Lê 13 apostas e armazena todas
apostas = []
pontuacao=[]
for i in range(1,13):
    aposta = int(input("Insira sua aposta: "))
    apostas.append(aposta)
# Verifica se cada aposta está na matriz
for aposta in apostas:
    if aposta in matriz:
        print(f"O número {aposta} está na matriz ✅")
        pontuacao.append(aposta)
    else:
        print(f"O número {aposta} NÃO está na matriz ❌")

print(f"Pontuação feita pelo jogador: {len(pontuacao)}")