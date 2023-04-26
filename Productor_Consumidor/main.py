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