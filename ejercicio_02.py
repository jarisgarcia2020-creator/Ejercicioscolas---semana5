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

#Imprime la cantidad de elementos de la cola.
cola = crear_cola([10, 20, 30, 40, 50])

if cola.is_empty():
    print("La cola está vacía.")
else:
    print("Cantidad de elementos:", cola.size())
