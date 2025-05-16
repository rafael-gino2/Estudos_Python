# 2-Crie uma função que receba um número e informe se ele é par ou ímpar.
num = int(input("Digite um número: "))

def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
par_ou_impar(num)