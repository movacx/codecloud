# from View.carrera_view import CarreraView
# from Model.carrera import Carrera
# from Model.corredor import Corredor

import threading
import time
from queue import Queue, Empty


class CarreraController:
    def __init__(self, carrera, vista):
        self.carrera = carrera
        self.vista = vista

        #lock para proteger la seccion critica
        self.lock = threading.Lock()
        #cola para enviar los eventos desde los hilos hacia la interfaz

        self.eventos = Queue()
        #Lista de hilos creados
        self.hilos=[]
        #Bandera de control
        self.detener=False

        self.configurar_vista()

    def _configurar_vista(self):
        '''Conecta botones y dibuja la escena inicial'''
        self.vista.btn_iniciar.config(command = self.iniciar_carrera)
        self.vista.btn_reiniciar.config(command = self.reiniciar)
        self.vista.dibujar_escena(self.carrera)

        #after() permite reiniciar periodicamente la cola desde el hilo principal de Tkinter

        self.vista.root.after(50, self.procesar_Eventos)

    def procesar_eventos(self):
        'Atiende los eventos enviados por los hilos Esta funcion se ejecuta repetidamente en el hilo principal de tkinter lo cual evita'
        'actualizar la interfaz directamente desde hilos secundarios'

        try:
            while True:
                #remueve y retorna un item de la cola
                evento = self.eventos.get_nowait()

                tipo = evento['tipo']
                if tipo == 'avance':
                    self.vista.actualizar_corredor(evento['nombre'], evento['posicion'])
                elif tipo == 'estado':
                    self.vista.mostrar_estado(evento['mensaje'])
                elif tipo == 'ganador':
                    self.vista.marcar_ganador(evento['nombre'])
                    self.vista.mostrar_estado(f'Gano {evento['nombre']} la carrera')
                    self.vista.activar_inicio()
        except Empty:
            pass

        #Se vuelve a ejecutar la revision de la cola

        self.vista.root.after(50, self.procesar_eventos())
    
    def mover_corredor(self, corredor):
        '''
        Funcion que ejecuta cada hilo cada corredor avanza enintervalos aleatorios y con pasos aleatorios
        '''

        while True:
            time.sleep(Random.uniform(0.08, 0.25))

            with self.lock:
                return #imcompleto