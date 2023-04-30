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