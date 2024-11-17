class Queue:
  def __init__(self):
    self.inbound_stack = []
    self.outbound_stack = []

  def enqueue(self, data):
    self.inbound_stack.append(data)
    
  def dequeue(self):
    if not self.outbound_stack:
      while self.inbound_stack:
        self.outbound_stack.append(self.inbound_stack.pop())
    return self.outbound_stack.pop()
'''
  def mostrar_outbound(self):
    print('Outbound')
    for i in self.outbound_stack:
      print(i)
  
  def mostrar_inbound(self):
    print('Inbound')
    for i in self.inbound_stack:
      print(i)
'''  

numbers = Queue()

numbers.enqueue(1)
numbers.enqueue(2)
numbers.enqueue(3)
print(f"Outbound: {numbers.outbound_stack}")
print(f"Inbound: {numbers.inbound_stack}")
print(f'dequeue: {numbers.dequeue()}') # Output: 1
print(f"Outbound: {numbers.outbound_stack}")
print(f"Inbound: {numbers.inbound_stack}")
print(f"dequeue: {numbers.dequeue()}") # Output: 2
print(f"Outbound: {numbers.outbound_stack}")
print(f"Inbound: {numbers.inbound_stack}")
numbers.enqueue(4)
numbers.enqueue(5)
print(f"Outbound: {numbers.outbound_stack}")
print(f"Inbound: {numbers.inbound_stack}")
print(f"dequeue: {numbers.dequeue()}")
print(f"Outbound: {numbers.outbound_stack}")
print(f"Inbound: {numbers.inbound_stack}")

