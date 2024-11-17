class NodoDobule:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0
    
  def enqueue(self, valor):
    new_node = NodoDobule(valor)
    if self.head is None:
      self.head = new_node
      self.tail = self.head
    else:
      new_node.anterior = self.tail
      self.tail.siguiente = new_node
      self.tail = new_node
    self.count += 1
    
  def dequeue(self):
    if self.head is None:
      return "Queue vacío"
    else:
      current = self.head
      self.head = self.head.siguiente
      if self.head is not None:
        self.head.anterior = None
      self.count -= 1     
    return current.valor
  
  def mostrar(self):
    current = self.head
    if current is None:
      print("Queue vacío")
      return
    while current is not None:
      print(current.valor)
      current = current.siguiente

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print()
print("Queue")
queue.mostrar()
print()
print(f'dequeue: {queue.dequeue()}')
print()
print('Queue')
queue.mostrar()
print()
print(f"dequeue: {queue.dequeue()}")
print()
print('Queue')
queue.mostrar()
print()
print(f"dequeue: {queue.dequeue()}")
print(queue.dequeue())  # Queue vacío
print()
print('Queue')
queue.mostrar()  # Queue vacío
