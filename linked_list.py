from nodos import Nodo

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, valor):
        nodo = Nodo(valor)

        if self.tail == None:
            self.head = nodo
            self.tail = nodo
        else:
            self.tail.siguiente = nodo

            while self.tail.siguiente:
                self.tail = self.tail.siguiente

            self.tail = nodo
        self.size += 1

    def size(self):
        return str(self.size)

    def iter(self):
        current = self.head

        while current:
            val = current.valor
            current = current.siguiente
            yield val

    def delete(self, valor):
        current = self.head
        prev = self.head

        while current:
            if current.valor == valor:
                if current == self.head:
                    self.head = current.siguiente
                else:
                    prev.siguiente = current.siguiente
                    self.size -= 1
                    print(f'Valor {valor} eliminado')
                    return current.valor
            prev = current
            current = current.siguiente

    def search(self, valor):
        for nodo in self.iter():
            if valor == nodo:
                print(f'Valor {valor} encontrado')
                return True
        print(f'Valor {valor} no encontrado')
        return False

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        return str(self.valor)
