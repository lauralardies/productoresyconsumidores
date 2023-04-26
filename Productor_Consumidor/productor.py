from .recurso import *
import random
import time

def productor(id):
    global buffer, mutex_procons, max
    while buffer.total < max:
        milisegs = random.randint(100, 500) # Generar un tiempo de espera aleatorio
        time.sleep(milisegs/1000.0) # Esperar el tiempo aleatorio generado
        mutex_procons.acquire()
        if buffer.total < max:
            valor_producido = id * 100 + buffer.total
            buffer.buff[buffer.posactual] = valor_producido
            buffer.posactual += 1
            if buffer.posactual == TAMBUFF:
                buffer.posactual = 0
            buffer.total += 1
            print(f'Productor {id} produjo {valor_producido}.')
        mutex_procons.release()