'''
Ejemplo 3: Sincronizacion usando lock
Este archivo muestra por que se necesita sincronizacion cuando varios hilos comparten el mismo recurso
En este ejejmplo, varios hilos actualizan una variable compartida.
Se usa un lock para evitar que dos hilos modifiquen la variable exactamente al mismo tiempo
'''

import threading
import time

#Recurso compartido
contador = 0

#Lock para controlar el acceso al recurso compartido

candado = threading.Lock()

def incrementar(nombre):
    '''
    Funcion que incrementa la variable global 'contador'
    El Lock garantiza que solo un hilo a la vez oueda entrar a la seccion critica
    '''

    global contador
    for i in range(5):
        with candado:
            valor_actual = contador
            print(f'{nombre} lee contador = {valor_actual}')

            #Se simula un peque;o retraso para hacer mas evidente el problema de concurrencia
            time.sleep(0.5)

            contador = valor_actual + 1
            print(f'{nombre} actualiza contador a {contador}')

    print('inicio del programa')
hilo1 = threading.Thread(target=incrementar, args=('Hilo1',))
hilo2 = threading.Thread(target=incrementar, args=('Hilo2',))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(f'Valor final del contador: {contador}')
print('fin del programa')