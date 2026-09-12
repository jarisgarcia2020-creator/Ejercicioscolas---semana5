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

#Se coloca en el frente el primer nombre que inicia con A.
cola = crear_cola(["Luis", "Ana", "Carlos", "Andrea", "Pedro"])

if cola.is_empty():
    print("La cola está vacía.")
else:
    temporal = Queue()
    seleccionado = None

    while not cola.is_empty():
        nombre = cola.dequeue()

        if seleccionado is None and nombre.upper().startswith("A"):
            seleccionado = nombre
        else:
            temporal.enqueue(nombre)

    if seleccionado is None:
        while not temporal.is_empty():
            cola.enqueue(temporal.dequeue())
        print("No se encontró un nombre que inicie con A.")
    else:
        cola.enqueue(seleccionado)
        while not temporal.is_empty():
            cola.enqueue(temporal.dequeue())

        print("Cola resultante:", mostrar_cola(cola))
