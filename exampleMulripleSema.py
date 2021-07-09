import argparse
import pandas as pd
import numpy as np 
from concurrent.futures import ThreadPoolExecutor
import sys
import time
import concurrent.futures
import threading

buffer = []
semaProducer = threading.BoundedSemaphore(value=1)
# El count puede varia dependiendo si se usa alternacia o no
semaProdCon = threading.BoundedSemaphore(value=1)


def readDataProducer(thread_number):
    print("Thread {} esta tratando de utilizar el recurso compartido ".format(thread_number))

    # Ir a traer al dataframe la infomacion 
    semaProducer.acquire() #El condicional esta explicito
    print("Thread {} puede usar el DF recurso compartido ".format(thread_number))
    # Ir a traer al datafame una fila y elminar esta del dataframe
    time.sleep(10)
    print("Thread {} Liberando el dataframe ".format(thread_number))
    semaProducer.release()
    
    # ir a meter al buffer
    semaProdCon.acquire() # verificamos si el recurso compartio esta disponible
    print("Thread {} puede usar el BUFFER recurso compartido ".format(thread_number))
    time.sleep(5)
    print("Thread {} Liberando el buffer ".format(thread_number))
    semaProdCon.release()




if __name__ == "__main__":

    for thread_number in range(10):
        t = threading.Thread(target=readDataProducer, args=(thread_number,))
        t.start()
        time.sleep(1)



