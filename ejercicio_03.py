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

#Se coloca en el fondo de la cola el número mayor.
cola = crear_cola([12, 5, 27, 8, 19])

if cola.is_empty():
    print("La cola está vacía.")
else:
    temporal = Queue()
    mayor = cola.front()

    while not cola.is_empty():
        elemento = cola.dequeue()
        if elemento > mayor:
            mayor = elemento
        temporal.enqueue(elemento)

    encontrado = False
    while not temporal.is_empty():
        elemento = temporal.dequeue()
        if elemento == mayor and not encontrado:
            encontrado = True
        else:
            cola.enqueue(elemento)

    cola.enqueue(mayor)
    print("Cola resultante:", mostrar_cola(cola))
