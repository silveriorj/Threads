from threading import Thread, RLock, Lock
import time
import random

class Acumuladora(Thread):
    def __init__(self, lock, recurso):
        Thread.__init__(self)

        self.rlock = rlock
        self.recurso = recurso

    def acumula(self):
        
        self.rlock.acquire()
        ## regiao critica
        self.recurso+=1
        ## fim da regiao critica
        self.rlock.release()

    def run(self):

        for i in range(20):
            self.rlock.acquire()
            self.acumula()
            self.rlock.release()
            
            
class Olx(Thread):
    def __init__(self, lock, recurso):
        Thread.__init__(self)

        self.rlock = rlock
        self.recurso = recurso

    def desacumula(self):
        
        self.rlock.acquire()
        ## regiao critica
        self.recurso+=1
        ## fim da regiao critica
        self.rlock.release()

    def run(self):

        for i in range(20):
            self.rlock.acquire()
            self.desacumula()
            self.rlock.release()


if __name__ == "__main__":
    recurso = 0
    rlock=RLock()

    t1 = Acumuladora(rlock, recurso)
    t2 = Olx(rlock, recurso)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Resultado final {}".format(recurso))