# 7. Utilizando a lógica anterior modifique a função velocidade_media() utilizando uma
# função divisao() para calcular a velocidade. A função divisao() recebe dois números
# como parâmetros, calcula e retorna o resultado da divisão do primeiro pelo segundo.
def divisao(distancia, tempo):
    if tempo == 0:
        return "Divisão por zero não é permitida."
    return distancia / tempo

def velocidade_media(distancia, tempo):
    return divisao(distancia, tempo)

distancia = 150  # metros
tempo = 15  # segundos

print(f"Velocidade média: {velocidade_media(distancia, tempo)} m/s")
