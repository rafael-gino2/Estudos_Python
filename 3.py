# 3 - Crie uma função que receba uma lista de números e retorne a soma de todos
# os números ímpares da lista.
def soma_impares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 != 0:
            soma += numero
    return soma
numeros = [1, 2, 3, 4, 5, 6, 7]
resultado = soma_impares(numeros)
print("Soma dos números ímpares:", resultado)
