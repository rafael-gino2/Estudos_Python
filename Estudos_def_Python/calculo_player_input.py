jogadores = []

qnt_players = int(input("Insira a quantidade de jogadores a adicionar: "))

for i in range(qnt_players):
    nome = input("Insira o nome do jogador: ")
    gols = int(input("Insira a quantidade de gols: "))
    assistencias = int(input("Insira a quantidade de assistencias: "))
    pontuacao = (gols * 5) + (assistencias * 3)
    jogador = {'nome': nome, 'gols': gols, 'assistencias': assistencias, 'pontuacao': pontuacao}
    jogadores.append(jogador)

jogadores.sort(key=lambda x: (x['pontuacao'],x['gols'], x['assistencias']), reverse=True) # aqui é utilizado o sort para ordenar a pontuação de cada jogador (por meio do uso do lambda que usamos para filtrar pelo indice de pontuacao, e caso a pontaução seja igual desempata por qnt de gols ou assistencias em terceiro caso) e tbm utilizamos o reverse=True para deixar em ordem Decrescente
print(jogadores)
