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

#Sacar de la cola todos los ceros sin modificar la cola original
cola = crear_cola([4, 0, 7, 0, 2, 0, 9])

if cola.is_empty():
    print("La cola está vacía.")
else:
    sin_ceros = Queue()
    temporal = Queue()

    while not cola.is_empty():
        elemento = cola.dequeue()
        temporal.enqueue(elemento)

        if elemento != 0:
            sin_ceros.enqueue(elemento)

    #Restaurar la cola original exactamente como estaba.
    while not temporal.is_empty():
        cola.enqueue(temporal.dequeue())

    print("Cola original (sin modificar):", mostrar_cola(cola))
    print("Cola temporal sin ceros:", mostrar_cola(sin_ceros))
