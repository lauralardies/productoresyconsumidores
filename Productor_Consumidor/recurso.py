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