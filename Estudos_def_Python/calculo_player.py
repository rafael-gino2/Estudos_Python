jogadores = [
    {"nome": "Messi", "gols": 2, "assistencias": 1},
    {"nome": "Neymar", "gols": 1, "assistencias": 2},
    {"nome": "Mbappe", "gols": 3, "assistencias": 0},
    {"nome": "Vini Jr", "gols": 1, "assistencias": 1}
]


for i in jogadores:
    pontuacao = (i["gols"] * 5 + i["assistencias"] * 3)
    i.setdefault('pontuacao') #usando o setdefault para criar uma nova variavel no dicionario sem nenhum valor (em None)
    i['pontuacao'] = pontuacao

jogadores.sort(key=lambda x: x['pontuacao'], reverse=True) # aqui é utilizado o sort para ordenar a pontuação de cada jogador (por meio do uso do lambda que usamos para filtrar pelo indice de pontuacao) e tbm utilizamos o reverse=True para deixar em ordem Decrescente
print(jogadores)