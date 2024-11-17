from nodos import Nodo

head = None
tail = None
size = 0

for valor in range(1, 6):

  if head is None:
    head = tail = Nodo(valor)
  else:
    current = Nodo(valor)
    tail.siguiente = current
    current.anterior = tail
    tail = current
    
  tail.siguiente = head
  head.anterior = tail
  size += 1

    
  print(f'Nodo {size} con valor {valor} creado con éxito')

print(f'Head: {head.valor}, Tail: {tail.valor}')
print(f'Size: {size}')
print()

print('Lista enlazada:')
current = head
fin = tail
while fin != head:
    print(current.valor)
    current = current.siguiente
    fin = current
print()

#lista circular
print (f'Head Previous: {head.anterior.valor}, Tail Next: {tail.siguiente.valor}')
    