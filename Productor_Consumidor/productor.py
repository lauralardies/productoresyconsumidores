from globals import *
from recurso import *
import random
import time

def productor(id):
    maxResources = globals.maxResources
    buffer = globals.buffer
    mutex_procons = globals.mutex_procons
    TAMBUFF = globals.TAMBUFF
    while buffer.total < maxResources:
        milisegs = random.randint(100, 500) # Generar un tiempo de espera aleatorio
        time.sleep(milisegs/1000.0) # Esperar el tiempo aleatorio generado
        mutex_procons.acquire()
        if buffer.total < maxResources:
            valor_producido = id * 100 + buffer.total
            buffer.buff[buffer.posactual] = valor_producido
            buffer.posactual += 1
            if buffer.posactual == TAMBUFF:
                buffer.posactual = 0
            buffer.total += 1
            print(f'Productor {id} produjo {valor_producido}.')
        mutex_procons.release()