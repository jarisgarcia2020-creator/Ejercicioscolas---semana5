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

#Se escribe un algoritmo que invierta los elementos de una cola.
cola = crear_cola([1, 2, 3, 4, 5])

if cola.is_empty():
    print("La cola está vacía.")
else:
    
    invertida = Queue()

    while not cola.is_empty():
        temporal = Queue()

        while cola.size() > 1:
            temporal.enqueue(cola.dequeue())

        ultimo = cola.dequeue()
        invertida.enqueue(ultimo)

        while not temporal.is_empty():
            cola.enqueue(temporal.dequeue())

    while not invertida.is_empty():
        cola.enqueue(invertida.dequeue())

    print("Cola invertida:", mostrar_cola(cola))
