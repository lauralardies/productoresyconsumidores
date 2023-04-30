# productoresyconsumidores

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/productoresyconsumidores)
https://github.com/lauralardies/productoresyconsumidores

## Breve introducción
Este ejercicio nos presenta el problema de productor-consumidor y cómo resolverlo.
¿En qué consiste el **problema productor-consumidor**?
El productor provee recursos y el consumidor hace uso de dichos recursos. Sin embargo, puede pasar que el productor provea más rápido de lo que el consumidor pueda aceptar o que el consumidor consuma más rápido de lo que el productor pueda aportar. En ambos casos se crea un problema que solucionamos creando equilibrio entre los dos elementos (producir y consumir a la misma velocidad).

## Cómo ejecutar el código
Para ejecutar el código, se debe abrir la terminal e introducir la siguiente línea:
```
cd Productor_Consumidor
```
Esta línea nos permite acceder a la carpeta `Productor_Consumidor`.
El siguiente paso para poder ejecutar nuestro código es escribir el siguiente comando después de haber accedido a nuestra carpeta.
```
python3 main.py [total del productores] [total de consumidores] [max]
```
Siendo `[total del productores]` y `[total de consumidores]` los argumentos de línea de comando para el número total de productores y consumidores, respectivamente.

## Código
Todos los archivos están guardados en la carpeta `Productor_Consumidor`.

### Código `globals.py`
```
class Globals():
    TAMBUFF = None
    buffer = None
    mutex_procons = None
    maxResources = None

globals = Globals()
```

### Código `recurso.py`
```
import threading
from globals import *

globals.TAMBUFF = 30

class Recurso:
    def __init__(self):
        self.buff = [0] * globals.TAMBUFF
        self.posactual = 0
        self.total = 0

globals.buffer = Recurso()
globals.mutex_procons = threading.Lock()
```

### Código `productor.py`
```
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
            valor_producido = id + buffer.total
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
    mutex_procons = globals.mutex_procons
    buffer = globals.buffer
    TAMBUFF = globals.TAMBUFF
    while True:
        milisegs = random.randint(100, 500) # Generar un tiempo de espera aleatorio
        time.sleep(milisegs/1000.0) # Esperar el tiempo aleatorio generado
        mutex_procons.acquire()
        if buffer.total > 0:
            valor_consumido = buffer.buff[(buffer.posactual - buffer.total + TAMBUFF) % TAMBUFF]
            buffer.total -= 1
            print(f'Consumidor {id} consumió {valor_consumido}.')
        mutex_procons.release()
        break
```

### Código `main.py`
```
from globals import *
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
globals.maxResources = int(sys.argv[3])

globals.buffer = Recurso()
globals.mutex_procons = threading.Lock()

inicio = time.time()

threads = []
for i in range(totprod):
    t = threading.Thread(target=productor, args=(i,))
    threads.append(t)
    t.start()

for i in range(totcons):
    t = threading.Thread(target=consumidor, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

fin = time.time()
print(f"Tiempo total de ejecución: {fin - inicio} segundos")
```
