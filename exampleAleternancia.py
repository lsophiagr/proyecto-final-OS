import argparse
import pandas as pd
import numpy as np 
from concurrent.futures import ThreadPoolExecutor
import sys
import time
import concurrent.futures
import threading


bufferSize = 2
buffer = []
semaProducer = threading.BoundedSemaphore(value=1)
# El count puede varia dependiendo si se usa alternacia o no
semaProdProd = threading.BoundedSemaphore(value=1)
semaConCon = threading.BoundedSemaphore(value=1)

semaAleterProdCon = threading.BoundedSemaphore(value=1)

# No puede producir mas cuando el buffer este lleno
# Ya no tenga datos que producir
def productorAlter(thread_number):
    # Un wihile mientras la variable del len sea distinto a 0
    
    semaAleterProdCon.acquire()

    print("Productor Thread {} esta tratando de utilizar el recurso compartido ".format(thread_number))

    # Ir a traer al dataframe la infomacion 
    semaProducer.acquire() #El condicional esta explicito
    print("Productor Thread {} puede usar el DF recurso compartido ".format(thread_number))
    # Ir a traer al datafame una fila y elminar esta del dataframe
    time.sleep(1)
    print("Productor Thread {} Liberando el dataframe ".format(thread_number))
    semaProducer.release()
    

    
    # ir a meter al buffer
    semaProdProd.acquire() # verificamos si el recurso compartio esta disponible
    print("Productor Thread {} puede usar el BUFFER recurso compartido ".format(thread_number))
    if (len(buffer) <= bufferSize): # Si es menor esto quiere decir que le queda espacio al buffer por lo que puede meter datos todavia.
        time.sleep(1)
        print("Productor Thread {} Realizo  operacion con el buffer y lo libero".format(thread_number))
        semaProdProd.release()
        if (len(buffer) == bufferSize):  
            print("Se lleno el buffer")
            semaAleterProdCon.release()
    else:
        print("Productor Thread {} Liberando BUFFER LLENO".format(thread_number))
        semaProdProd.release()


# un consumidor no se puede ejecutar si el buffer esta vacio
# que pasa cuando por casualidad en lugar de iniciar un productor inicia un consumidor? este no puede hacer nada
def consumidorAlert(thread_number):

    semaAleterProdCon.acquire()
    # genear Los nuevos registros de compras
    print("Consumidor Thread {} esta tratando Leer el BUFFER ".format(thread_number))
    semaConCon.acquire() # verificamos si el BUFFER compartio esta disponible

    if not buffer:
        print("Consumidor Thread {} Liberado BUFFER VACIO ".format(thread_number))
        semaConCon.release()
        semaAleterProdCon.release()
    else:  
        print("Consumidor Thread {} puede usar el BUFFER recurso compartido ".format(thread_number))
        time.sleep(5)
        print("Consumidor Thread {} Liberando el buffer ".format(thread_number))
        semaConCon.release()
    
def creteThreadsProducer(n):
    print('inicio de theread productores correctamente')
    for thread_number in range(n):
        t = threading.Thread(target=productorAlter, args=(thread_number,))
        t.start()
        time.sleep(1)

def creteThreadsConsumer(n):
    print('inicio de thread consumidores correctamente')
    for thread_number in range(n):
        t = threading.Thread(target=consumidorAlert, args=(thread_number,))
        t.start()
        time.sleep(1)

if __name__ == "__main__":
    tp = threading.Thread(target=creteThreadsProducer, args=(5,))
    tc = threading.Thread(target=creteThreadsConsumer, args=(2,))
    tp.start()
    tc.start()



