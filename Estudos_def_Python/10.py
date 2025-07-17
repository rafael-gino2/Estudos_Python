# Caixa eletronico que diz a quantidade de cada nota do saque
notas = [100,50,20,10,5,2]

def caixa_eletronico():
  while True:
    try:
      valor = int(input("Digite o valor para saque: "))
      if valor > 0:
        print('Simulador de Caixa Eletrônico')
        print('-----------------------------')

        if valor < 2:
          print("Digite um valor acima de 2 reais")
        else:
          for nota in notas:
            quantidade = valor // nota
            valor = valor % nota
            print(f'Precisa de {quantidade} de {nota}')
      else:
        print("Informe um valor acima de 0")
    except ValueError:
      print("Erro! Insira um valor válido")
    continua = input("Deseja continuar? (s/n)")
    if continua == 'n':
      break