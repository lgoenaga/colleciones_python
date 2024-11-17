from nodos import Nodo

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, valor):
        nodo = Nodo(valor)
        self.size += 1
        if self.top is None:
            self.top = nodo
        else:
            current = nodo
            current.siguiente = self.top
            self.top = current

    def pop(self):
        if self.top:
            valor = self.top.valor
            self.top = self.top.siguiente
            self.size -= 1
            return f"Valor {valor} eliminado"
        else:
            self.top = None
            return "Stack vacío"

    def peek(self):
        if self.top:
            return f"Top: {self.top.valor}"
        else:
            return "Stack vacío"

    def __len__(self):
        return self.size

    def __str__(self):
        current = self.top
        stack = []
        while current:
            stack.append(current.valor)
            current = current.siguiente
        return str(stack)

    def clear(self):
        self.top = None
        self.size = 0
        return "Stack vaciado"

    def search(self, valor):
        current = self.top
        index = 0
        while current:
            if current.valor == valor:
                return f"Valor {valor} encontrado en la posición {index}"
            current = current.siguiente
            index += 1
        return "Valor no encontrado"

    def listar(self):
        current = self.top
        pila = []
        while current:
            pila.append(current.valor)
            current = current.siguiente
        return ", ".join(map(str, pila))

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print()
print(stack)  # [3, 2, 1]
print()
print(stack.search(2))  # Valor 2 encontrado en la posición 1
print()
print(stack.listar())  # 3, 2, 1
print()
print(stack.peek())  # 3
print()
print(stack.pop())  # 3
print()
print(stack)  # [2, 1]
print()
print(len(stack))  # Tamaño: 2
print()
stack.clear()
print(stack)  # []
print(stack.pop())  # Stack vacío
print(stack.peek())  # Stack vacío
print()
print(stack.search(2))  # Valor no encontrado
print()
print(len(stack))  # 0
