# calculando média de notas
somando = 0
cont = 1
qnt_provas = int(input("Quantas provas vc quer?: "))

while cont <= qnt_provas:
  nota27 = float(input("Insira sua nota: "))
  cont += 1
  somando += nota27

media_do_aluno = somando/qnt_provas
print(f"A sua é média de notas é {media_do_aluno}")