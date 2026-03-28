jogadores = [
    {"nome": "Messi", "gols": 2, "assistencias": 3},
    {"nome": "Neymar", "gols": 1, "assistencias": 2},
    {"nome": "Mbappe", "gols": 3, "assistencias": 1},
    {"nome": "Vini Jr", "gols": 1, "assistencias": 1}
]

for i in jogadores:
    pontuacao = (i["gols"] * 5 + i["assistencias"] * 3)
    i.setdefault('pontuacao') #usando o setdefault para criar uma nova variavel no dicionario sem nenhum valor (em None)
    i['pontuacao'] = pontuacao

jogadores.sort(key=lambda x: (x['pontuacao'],x['gols'], x['assistencias']), reverse=True) # aqui é utilizado o sort para ordenar a pontuação de cada jogador (por meio do uso do lambda que usamos para filtrar pelo indice de pontuacao, e caso a pontaução seja igual desempata por qnt de gols ou assistencias em terceiro caso) e tbm utilizamos o reverse=True para deixar em ordem Decrescente
print(jogadores)