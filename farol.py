from threading import Thread,Condition
import time
import random


class Produtor(Thread):

    def __init__(self,recurso,condicao):
        Thread.__init__(self)
        self.recurso = recurso
        self.condicao = condicao
    
    def run(self):
        for x in range(5):
            self.condicao.acquire()
            i=random.randint(1,1000)
            print("Produzido {}".format(i))
            self.recurso.append(i)
            self.condicao.notify()
            self.condicao.release()
            time.sleep(2)

class Consumidor(Thread):

    def __init__(self,recurso,condicao):
        Thread.__init__(self)
        self.recurso = recurso
        self.condicao = condicao
    
    def run(self):
        for x in range(5):
            self.condicao.acquire()
            while True:
                if len(self.recurso)>0:
                    i=self.recurso.pop()
                    print("Consumindo {}".format(i))
                    break
                self.condicao.wait()
            self.condicao.release()
            time.sleep(3)

if __name__ == "__main__":

    recurso = []
    condicao = Condition()

    produtor = Produtor(recurso,condicao)
    consumidor = Consumidor(recurso,condicao)

    produtor.start()
    consumidor.start()

    produtor.join()
    consumidor.join()
