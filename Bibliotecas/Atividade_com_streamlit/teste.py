import csv

with open('Matriculas_pii_none.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        print(linha)

