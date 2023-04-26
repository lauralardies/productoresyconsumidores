# productoresyconsumidores

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/productoresyconsumidores)
https://github.com/lauralardies/productoresyconsumidores

## Cómo ejecutar el código
Para ejecutar el código, se debe abrir **bash** (ni terminal, ni consola, etc.) e introducir la siguiente línea:
```
cd Productor_Consumidor
```
Esta línea nos permite acceder a la carpeta `Productor_Consumidor`.
El siguiente paso para poder ejecutar nuestro código es escribir el siguiente comando (todavía estamos en el bash) después de haber accedido a nuestra carpeta.
```
python main.py [total del productores] [total de consumidores]
```
Siendo `[total del productores]` y `[total de consumidores]` los argumentos de línea de comando para el número total de productores y consumidores, respectivamente.

## Código
Todos los archivos están guardados en la carpeta `Productor_Consumidor`.

### Código `recurso.py`
```
import threading

TAMBUFF = 30

class Recurso:
    def __init__(self):
        self.buff = [0] * TAMBUFF
        self.posactual = 0
        self.total = 0

buffer = Recurso()
mutex_procons = threading.Lock()
max = None
```

### Código `productor.py`
```
from recurso import *
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
```

### Código `consumidor.py`
```
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
```

### Código `main.py`
```
from recurso import *
from productor import *
from consumidor import *
import sys
import threading
import time

if len(sys.argv) != 4:
    print("Sintaxis: python " + sys.argv[0] + " <totprod> <totcons> <max>")
    sys.exit(1)

totprod = int(sys.argv[1])
totcons = int(sys.argv[2])
max = int(sys.argv[3])

buffer = Recurso()
mutex_procons = threading.Lock()
inicio = time.time()

threads = []
for i in range(totprod):
    t = threading.Thread(target=productor, args=(i,))
    threads.append(t)

for i in range(totcons):
    t = threading.Thread(target=consumidor, args=(i,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

fin = time.time()
print(f"Tiempo total de ejecución: {fin - inicio} segundos")
```
