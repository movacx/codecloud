'''
Ejemplo #2 multiples hilos
Este archivo muestra como varios hilos pueden ejecutarse de manera concurrente.
Cada hilo simula un trabajador realizando su tarea

'''

import threading
import time

def trabajador(nombre):
    '''
    Funcion qe ejecutara el hilo el nombre es usado para identificar cual hilo esta trabajando
    '''
    for i in range(1,4):
        print(f'{nombre} ejecutando paso {i}')
        time.sleep(1)

    print(f'{nombre} termino')
    print('iniciando multiples hilos..........')

hilo1 = threading.Thread(target=trabajador, args=('Hilo 1',))
hilo2 = threading.Thread(target=trabajador, args=('Hilo 2',))
hilo3 = threading.Thread(target=trabajador, args=('Hilo 3',))

#Se inician los hilos
hilo1.start()
hilo2.start()
hilo3.start()

#El programa principal espera a que todos
hilo1.join()
hilo2.join()
hilo3.join()

print('Todos los hilos finalizaron')