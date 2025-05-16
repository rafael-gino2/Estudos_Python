# 5. Refaça a lógica anterior, porém para a multiplicação deve ser feita utilizando seguidas
# somas.
def escolhas():
  num1 = int(input("Insira seu primeiro número aqui: "))
  num2 = int(input("Insira seu segundo número aqui: "))
  operacao = input("Qual operação quer usar?? (+,-,x,/,%)")
  return num1, num2, operacao

def multi(num1,num2):
  resultado = 0
  for i in range(num2):
    resultado = resultado + num1
  return resultado

def operacoes(num1, num2,operacao):
  if operacao == "x":
      resultado = multi(num1, num2)
      print("Resultado:", resultado)
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