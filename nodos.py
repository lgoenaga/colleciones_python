

class Nodo():
    def __init__(self, valor, siguiente=None, anterior=None):
        self.valor = valor
        self.siguiente = siguiente
        self.anterior = anterior

    def __str__(self):
        return str(self.valor)