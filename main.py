import argparse
from datetime import datetime
import pandas as pd
import numpy as np 
from concurrent.futures import ThreadPoolExecutor
import sys
import time
import concurrent.futures
import threading
import random
from datetime import date

# Argumentos de la aplicacion mandar 0 si es nulo el consumidor
parser = argparse.ArgumentParser()
parser.add_argument("buffsize", type=int, help='buffsize for the problem')
parser.add_argument("productores",  type=int, help='Number of producer')
parser.add_argument("consumidor", help='Name of the CSV file for buyers')
parser.add_argument("alternancia",  type=int, help='Binari for alternancia')
args = parser.parse_args()
bufferSize = args.buffsize
nProductores = args.productores
# Si se quiere mandar el nombre del archivo de consumidor colocar 0 en el argumento
fileConsumidor = str(args.consumidor)
dfConsumidor = pd.read_csv(fileConsumidor)
nConsumidor = len(dfConsumidor)
print(nConsumidor)
boolAlter = args.alternancia
buffer = []

# contadorConsumidor = 0
# contadorProductor = 0

# Leer csv para productor
df = pd.read_csv('personas.csv')
df = df[['id', 'nombre', 'telefono', 'fecha', 'ciudad']]
dfArray = df.values.tolist()
constLenDf = len(dfArray)
# Declaracion de semaforos cuando La alternancia es 0
semaProducer = threading.BoundedSemaphore(value=1)
# El count puede varia dependiendo si se usa alternacia o no
semaProdCon = threading.BoundedSemaphore(value=1)

# Declaracion de semaforos cuando la alternacia es 1
semaProdProd = threading.BoundedSemaphore(value=1)
semaConCon = threading.BoundedSemaphore(value=1)
semaAleterProdCon = threading.BoundedSemaphore(value=1)


###### FUNCIONES PARA NO ALTERNANCIA ###########
# No puede producir mas cuando el buffer este lleno
# Ya no tenga datos que producir
def productor(thread_number):
    while (True):
        # While para recorer toda la data
        print("------Productor Thread {} esta tratando de utilizar el recurso compartido ------------".format(thread_number))
        # Ir a traer al dataframe la infomacion 
        semaProducer.acquire() #El condicional esta explicito, preguntamos al recurso (data frame) si esta en uso de no ser asi nosotros accesamos
        print("Productor Thread {} puede usar el DF recurso compartido ".format(thread_number))
        # Ir a traer al datafame una fila y elminar esta del dataframe

        print(len(dfArray))
        if(len(dfArray) == 0):
            nRandom = 0
        else:
            nRandom = random.randrange(len(dfArray))
        dataBonita = dfArray[nRandom]
        dfArray.pop(nRandom)
        print("Productor Thread {} Liberando el dataframe ".format(thread_number))
        semaProducer.release()
        
        # ir a meter al buffer
        semaProdCon.acquire() # verificamos si el recurso compartio esta disponible BUFFER
        print("Productor Thread {} puede usar el BUFFER recurso compartido ".format(thread_number))
        if (len(buffer) < bufferSize): # Si es menor esto quiere decir que le queda espacio al buffer por lo que puede meter datos todavia.
            buffer.append(dataBonita)
            print("Productor Thread {} Realizo  operacion con el buffer y lo libero".format(thread_number))
            semaProdCon.release()
        else:
            print("Productor Thread {} Liberando BUFFER LLENO".format(thread_number))
            print("LLENO LENO LLENO LLENO".format(thread_number))
            print(buffer)
            semaProdCon.release()
            
            if (nConsumidor == 0):
                exit()


# un consumidor no se puede ejecutar si el buffer esta vacio
# que pasa cuando por casualidad en lugar de iniciar un productor inicia un consumidor? este no puede hacer nada
def consumidor(thread_number):
    while(True):
        # genear Los nuevos registros de compras
        print("------------- Consumidor Thread {} esta tratando Leer el BUFFER -------------------- ".format(thread_number))
        semaProdCon.acquire() # verificamos si el BUFFER compartio esta disponible

        if not buffer:
            print("Consumidor Thread {} Liberado BUFFER VACIO ".format(thread_number))
            semaProdCon.release()
        else:  
            print("Consumidor Thread {} puede usar el BUFFER recurso compartido ".format(thread_number))
            dataCon = buffer.pop()
            precio = random.randrange(40,90)
            newArray = [dataCon[0], thread_number, precio, date.today()]
            print("Consumidor Thread {} Liberando el buffer ".format(thread_number))
            semaProdCon.release()

def creteThreadsProducer(n):
    print('inicio de theread productores correctamente')
    for thread_number in range(n):
        t = threading.Thread(target=productor, args=(thread_number,))
        t.start()
        # time.sleep(1)

def creteThreadsConsumer(n):
    print('inicio de thread consumidores correctamente')
    for thread_number in range(1, n+1):
        t = threading.Thread(target=consumidor, args=(thread_number,))
        t.start()
        # time.sleep(1)












# No puede producir mas cuando el buffer este lleno
# Ya no tenga datos que producir
def productorAlter(thread_number):
    
    semaAleterProdCon.acquire()
    a = 0
    # Un wihile mientras la variable del len sea distinto a 0
    while (a <= bufferSize):
        # While para recorer toda la data
        print("------Productor Thread {} esta tratando de utilizar el recurso compartido ------------".format(thread_number))
        # Ir a traer al dataframe la infomacion 
        semaProducer.acquire() #El condicional esta explicito, preguntamos al recurso (data frame) si esta en uso de no ser asi nosotros accesamos
        print("Productor Thread {} puede usar el DF recurso compartido ".format(thread_number))
        # Ir a traer al datafame una fila y elminar esta del dataframe

        print(len(dfArray))
        if(len(dfArray) == 0):
            nRandom = 0
        else:
            nRandom = random.randrange(len(dfArray))
        dataBonita = dfArray[nRandom]
        dfArray.pop(nRandom)
        a += 1
        print("Productor Thread {} Liberando el dataframe ".format(thread_number))
        semaProducer.release()
        
        # ir a meter al buffer
        semaProdCon.acquire() # verificamos si el recurso compartio esta disponible BUFFER
        print("Productor Thread {} puede usar el BUFFER recurso compartido ".format(thread_number))
        if (len(buffer) < bufferSize): # Si es menor esto quiere decir que le queda espacio al buffer por lo que puede meter datos todavia.
            buffer.append(dataBonita)
            print("Productor Thread {} Realizo  operacion con el buffer y lo libero".format(thread_number))
            semaProdCon.release()
        else:
            print("Productor Thread {} Liberando BUFFER LLENO".format(thread_number))
            print("LLENO LENO LLENO LLENO".format(thread_number))
            print(buffer)
            semaProdCon.release()
            
            if (nConsumidor == 0):
                exit()
    semaAleterProdCon.release()





# un consumidor no se puede ejecutar si el buffer esta vacio
# que pasa cuando por casualidad en lugar de iniciar un productor inicia un consumidor? este no puede hacer nada
def consumidorAlert(thread_number):

    semaAleterProdCon.acquire()
    b = 0
    while (b <= bufferSize):
        # genear Los nuevos registros de compras
        print("------------- Consumidor Thread {} esta tratando Leer el BUFFER -------------------- ".format(thread_number))
        semaProdCon.acquire() # verificamos si el BUFFER compartio esta disponible

        if not buffer:
            print("Consumidor Thread {} Liberado BUFFER VACIO ".format(thread_number))
            semaProdCon.release()
            b += 1
        else:  
            print("Consumidor Thread {} puede usar el BUFFER recurso compartido ".format(thread_number))
            if(len(dfArray)== 0):
                exit()
            else:
                dataCon = buffer.pop()
                precio = random.randrange(40,90)
                newArray = [dataCon[0], thread_number, precio, date.today()]
            print("Consumidor Thread {} Liberando el buffer ".format(newArray))
            semaProdCon.release()

    semaAleterProdCon.release()









def alterCreteThreadsProducer(n):
    print('inicio de theread productores correctamente')
    for thread_number in range(n):
        t = threading.Thread(target=productorAlter, args=(thread_number,))
        t.start()

def alterCreteThreadsConsumer(n):
    print('inicio de thread consumidores correctamente')
    for thread_number in range(n):
        t = threading.Thread(target=consumidorAlert, args=(thread_number,))
        t.start()



if __name__ == "__main__":

    
    if (boolAlter):
        print('ES ALETERNANCIA')
        while(len(dfArray)> 1):
            tp = threading.Thread(target=alterCreteThreadsProducer, args=(nProductores,))
            tc = threading.Thread(target=alterCreteThreadsConsumer, args=(nConsumidor,))
            tp.start()
            tc.start()




    else:
        print('NO NO ES ALETERNANCIA')
        # tp = threading.Thread(target=creteThreadsProducer, args=(nProductores,))
        # tc = threading.Thread(target=creteThreadsConsumer, args=(nConsumidor,))
        # tp.start()
        # tc.start()


        print('inicio de theread productores correctamente')
        for thread_number in range(nProductores):
            t = threading.Thread(target=productor, args=(thread_number,))
            t.start()
            # time.sleep(1)


        print('inicio de thread consumidores correctamente')
        for thread_number in range(nConsumidor):
            t = threading.Thread(target=consumidor, args=(thread_number,))
            t.start()
            # time.sleep(1)
        while (len(dfArray) > 0):
            print('Hola sigue vivo el main tread')




