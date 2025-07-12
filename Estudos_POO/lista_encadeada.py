class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

class Lista_encadeada_dupla:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def adicionando_inicio(self, valor):
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo_no
        else:
            novo_no.proximo = self.cabeca
            self.cabeca.anterior = novo_no
            self.cabeca = novo_no



lista = Lista_encadeada_dupla()
lista.adicionando_inicio(10)
def imprimir_lista(self):
        atual = self.cabeca
        while atual:
            print(atual.valor, end=" <-> ")
            atual = atual.proximo
        print("None")
