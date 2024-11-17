from nodos import Nodo

head = None
tail = None
size = 0

for valor in range(1, 6):
    if head is None:
        head = tail = Nodo(valor, None, None)
    else:
        current = Nodo(valor, None, tail)
        tail.siguiente = current
        tail = current
    size += 1
    print(f'Nodo {valor} creado')

print(f'Head: {head.valor}, Tail: {tail.valor}')
print(f'Size: {size}')
print()

print('Lista enlazada:')
current = head
while current is not None:
    print(current.valor)
    current = current.siguiente
print()

print('Lista enlazada (reversa):')
current = tail
while current is not None:
    print(current.valor)
    current = current.anterior
print()

# remove node
current = head
index = int(input('Ingrese el indice del nodo a eliminar: '))
pos = index
while current is not None and index > 1:
    current = current.siguiente
    index -= 1
if current is not None:
      #nodo_temp = current
      current.anterior.siguiente = current.siguiente
      current.siguiente.anterior = current.anterior
      size -= 1
      print()
      print(f'Nodo con valor {current.valor} en la posicion {pos} eliminado')
else:
  print('Nodo no encontrado')

print()
print("Lista enlazada:")
current = head
while current is not None:
    print(current.valor)
    current = current.siguiente
print()

# insert node
current = head
index = int(input('Ingrese el indice del nodo a insertar: '))
pos = index
while current is not None and index > 1:
    current = current.siguiente
    index -= 1
if current is not None:
    new_nodo = Nodo(2, current, current)
    current.anterior.siguiente = new_nodo
    current.anterior = new_nodo
    size += 1
    print()
    print(f'Nodo con valor {new_nodo.valor} insertado en la posicion {pos}')

print()
print("Lista enlazada:")
current = head
while current is not None:
    print(current.valor)
    current = current.siguiente
print()
