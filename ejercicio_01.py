from queue_structure import Queue

def crear_cola(valores):
    cola = Queue()
    for valor in valores:
        cola.enqueue(valor)
    return cola

def mostrar_cola(cola):
    
    temporal = Queue()
    elementos = []

    while not cola.is_empty():
        elemento = cola.dequeue()
        elementos.append(elemento)
        temporal.enqueue(elemento)

    while not temporal.is_empty():
        cola.enqueue(temporal.dequeue())

    return elementos

#Imprimir el primer elemento de la cola sin modificarla.
cola = crear_cola([10, 20, 30, 40])

if cola.is_empty():
    print("La cola está vacía.")
else:
    print("Primer elemento:", cola.front())

print("Cola después de la operación:", mostrar_cola(cola))
