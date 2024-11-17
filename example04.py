from nodos import Nodo

# Crear nodos
nodo1 = None
nodo2 = Nodo("A", None, None)
nodo3 = Nodo("B", nodo2, None)

print(nodo1)
print(nodo2)
print(nodo3)
print(nodo3.valor)
print(nodo3.siguiente)
print(nodo3.siguiente.valor)

head = None

for i in range(1,5):
    head = Nodo(i, head)
    
while head:
    print(head.valor)
    head = head.siguiente