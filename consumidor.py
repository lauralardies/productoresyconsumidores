from recurso import *
import random
import time

def consumidor(id):
    global buffer, mutex_procons
    while True:
        milisegs = random.randint(100, 500) # Generar un tiempo de espera aleatorio
        time.sleep(milisegs/1000.0) # Esperar el tiempo aleatorio generado
        mutex_procons.acquire()
        if buffer.total > 0:
            valor_consumido = buffer.buff[(buffer.posactual - buffer.total + TAMBUFF) % TAMBUFF]
            buffer.total -= 1
            print(f'Consumidor {id} consumió {valor_consumido}.')
        mutex_procons.release()
