# ProyectoFinal_OS
Repository created for the final project Operating systems

# Problema de sincronización de procesos 🧑🏻‍💻🚙🚗

El problema consiste en implementar el modelo de productor y consumidor en un buffer de tamaño limitado.Se debe generar un conjunto de leads para la compra de vehículos, los hilos productores comparten un archivo (personas.csv) que deben leer al azar hasta que se termine el archivo. Los productores no pueden enviar personas repetidas. Cada vez que un productor lee exitosamente un registro de personas deberá generar un lead para ser enviado a la cola de compradores donde un hilo consumidor vende un carro (los vendedores de vehículos adquieren a las personas)


# Problema Productor-Consumidor

El problema Productor-Consumidor es un problema clásico que se utiliza para la sincronización multiproceso, es decir, la sincronización entre más de un proceso.

En el problema productor-consumidor, hay un Productor que está produciendo algo y hay un Consumidor que está consumiendo los productos producidos por el Productor. Los productores y consumidores comparten el mismo búfer de memoria que es de tamaño fijo.

El trabajo del productor es generar los datos, ponerlos en el búfer y volver a comenzar a generar datos. Mientras que el trabajo del consumidor es consumir los datos del búfer.

# ¿Cuál es el problema aquí? 🧠👀
Los siguientes son los problemas que pueden ocurrir en el Productor-Consumidor:

1. El productor debe producir datos solo cuando el búfer no esté lleno. Si el búfer está lleno, no se le debería permitir al productor poner ningún dato en el búfer.
2. El consumidor debe consumir datos solo cuando el búfer no esté vacío. Si el búfer está vacío, no se debe permitir que el consumidor tome ningún dato del búfer.
3. El productor y el consumidor no deben acceder al búfer al mismo tiempo.

# Solución: Semáforos 🚨🚦🚥

Un semáforo es una variable que indica la cantidad de recursos que están disponibles en un sistema en un momento particular y esta variable de semáforo se usa generalmente para lograr la sincronización del proceso. Generalmente se denota por "S". Puede utilizar cualquier otro nombre de variable de su elección.

Un semáforo usa dos funciones, es decir, esperar () y señal (). Ambas funciones se utilizan para cambiar el valor del semáforo, pero el valor puede ser cambiado por un solo proceso en un momento particular y ningún otro proceso debe cambiar el valor simultáneamente.

La función wait () se usa para disminuir el valor de la variable de semáforo "S" en uno si el valor de la variable de semáforo es positivo. Si el valor de la variable del semáforo es 0, no se realizará ninguna operación.

La función signal () se utiliza para incrementar el valor de la variable del semáforo en uno.


# Preguntas a responder: 🤔❓
1. Cuantos leads compró cada consumidor
2. Cuantos leads creó cada productor
3. Cuanto tiempo promedio se tardó cada productor en producir un elemento
4. Cuanto tiempo le lleva a todo el sistema terminar de producir y consumir
5. Cuanto tiempo tarde en terminar el sistema en un modelo de alternancia
