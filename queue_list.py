class ListQueue:
    def __init__(self):
        self.list = []
        self.size = 0

    def enqueue(self, valor):
        self.list.append(valor)
        self.size += 1
        self.list.insert(0, valor+1) # Insertar el nuevo elemento al principio
        self.size += 1
        print()
        print(self.list) # Output: [2, 1]
        self.list.insert(0, self.list.pop())  # Mover el último elemento al principio
        print()
        print(self.list)
        print()
        # insertar el nuevo elemento al final
        self.list.insert(self.size, valor+2) # Insertar el nuevo elemento al final
        print()
        self.size += 1
        return self.list

    def dequeue(self):
        if self.size:
            #valor = self.list.pop(0) # Eliminar el primer elemento
            valor = self.list.pop() # Eliminar el último elemento
            self.size -= 1
            return f"Valor {valor} eliminado"
        else:
            return "Queue vacío"

    def peek(self):
        if self.size:
            print(f'Rear: {self.list[self.size-1]}') # Mostrar el último elemento
            return f"Front: {self.list[0]}" # Mostrar el primer elemento
        else:
            return "Queue vacío"
        
    def vaciar(self):
        self.list = []
        self.size = 0
        return "Queue vacío"

    def __len__(self):
        return self.size
      
    def mostrar(self):
        return self.list

    def __str__(self):
        return str(self.list)


queue = ListQueue()
print(queue.enqueue(1))
print(queue.enqueue(2))
print(queue.enqueue(3))
print()
print(f'dequeue: {queue.dequeue()}')
print(queue.peek())
print()
print(queue.mostrar())
print(f'len: {len(queue)}')
print()
print(f'dequeue: {queue.dequeue()}')
print(queue.peek())
print()
print(queue) 
print(f'len: {len(queue)}')
print()
print(queue.mostrar())
print()
print(queue.vaciar())
print(f'len: {len(queue)}')
print(queue.mostrar())  # Output: []  # Output: 0  # Output: []
