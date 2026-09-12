from queue_structure import Queue

def crear_cola(valores):
    cola = Queue()
    for valor in valores:
        cola.enqueue(valor)
    return cola

def mostrar_cola(cola):
    """Muestra una cola sin alterar su contenido ni su orden."""
    temporal = Queue()
    elementos = []

    while not cola.is_empty():
        elemento = cola.dequeue()
        elementos.append(elemento)
        temporal.enqueue(elemento)

    while not temporal.is_empty():
        cola.enqueue(temporal.dequeue())

    return elementos

#se realiza una cola temporal con las raíces cuadradas, sin modificar la cola original
import math

cola = crear_cola([1, 4, 9, 16, 25])
temporal = Queue()

if cola.is_empty():
    print("La cola original está vacía.")
else:
    restauracion = Queue()

    while not cola.is_empty():
        valor = cola.dequeue()
        restauracion.enqueue(valor)
        temporal.enqueue(math.sqrt(valor))

    # Restaurar la cola original.
    while not restauracion.is_empty():
        cola.enqueue(restauracion.dequeue())

    print("Cola original:", mostrar_cola(cola))
    print("Cola temporal con raíces:", mostrar_cola(temporal))
