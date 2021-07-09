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


def readDataProducer(thread_number):
    print("{} Este thread esta tratando de utilizar el recurso compartido ".format(thread_number))
    semaProducer.acquire() #El condicional esta explicito
    print("{} Se puede usar el recurso compartido ".format(thread_number))
    time.sleep(10)
    print("{} Liberando el recurso compartido ".format(thread_number))
    semaProducer.release()




if __name__ == "__main__":

    for thread_number in range(10):
        t = threading.Thread(target=readDataProducer, args=(thread_number,))
        t.start()
        time.sleep(1)



