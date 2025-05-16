# 4. Crie uma rotina de calculadora, onde receba dois valores e indique e receba qual
# operação básica deseja calcular, em seguida apresente o resultado. Todo o cálculo
# deve ser feito com uso de funções.
def escolhas():
  num1 = int(input("Insira seu primeiro número aqui: "))
  num2 = int(input("Insira seu segundo número aqui: "))
  operacao = input("Qual operação quer usar?? (+,-,x,/,%)")
  return num1, num2, operacao

def operacoes(num1, num2,operacao):
  if operacao == "x":
      print("Resultado:", num1 * num2)
  elif operacao == "+":
      print("Resultado:", num1 + num2)
  elif operacao == "-":
      print("Resultado:", num1 - num2)
  elif operacao == "/":
      print("Resultado:", num1 / num2)
  elif operacao == "%":
      print("Resultado:", num1 % num2)
  else:
      print("Operação inválida.")

num1, num2, operacao = escolhas()
operacoes(num1, num2, operacao)