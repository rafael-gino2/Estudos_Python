# 6. Defina uma função chamada velocidade_media() em um script que recebe dois
# parâmetros: a distância percorrida (em metros) e o tempo (em segundos) gasto.
distancia = 100  # metros
tempo = 10  # segundos
def velocidade_media(distancia, tempo):
    if tempo == 0:
        return "O tempo não pode ser zero."
    velocidade = distancia / tempo
    return velocidade



print(f"Velocidade média: {velocidade_media(distancia, tempo)} m/s")
