# adicionando filmes em uma lista
conta = 1
filmes = []
qnt_filmes = int(input("Quantos filmes você quer adicionar?: "))

while conta <= qnt_filmes:
  nome_filme = input("Insira o nome do filme: ")
  filmes.append(nome_filme)
  conta += 1

print(f"Filmes adicionados: {filmes}")