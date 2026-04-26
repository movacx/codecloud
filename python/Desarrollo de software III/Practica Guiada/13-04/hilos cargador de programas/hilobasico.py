"""
Ejemplo #1 Hilo basico en python
Este archivo muestra como crear un hilo sencillo usando threading
Objetivo:
    Como crear un hilo
    Como iniciar un hilo
    Como esperar a que termine

"""

import threading
import time

def tarea():
    '''
    El hio va a ejecutar esta funcion aca simulamos una tarea que tarda un poco
    en ejecutarse
    '''

    for i in range(1,100):
        print(f'Hilo trabajando... {i}')
        time.sleep(1)

    print('El hilo termino su trabajo')
print("Programa principal iniciado")

#Se crea el hilo indicando la funcion que va a ejecutar
hilo = threading.Thread(target=tarea)

#start()
hilo.start()
#join() #
# hace que el progrma principal espere hastta que el hilotermine
hilo.join()

print('programa principal finalizado')