from View.estudianteView import EstudianteGUI
import tkinter as tk
class EstudianteController:
    def __init__(self, root, service):
        self.GUI = EstudianteGUI(root, self)
        self.services = service

    def registrar_estudiante(self):
        try:
            carnet = self.GUI.carnet.get()
            nombre = self.GUI.nombre.get()
            carrera = self.GUI.carrera.get()

            exito = self.services.registro_estudiante(carnet, nombre, carrera)
            if exito:
                self.GUI.mostrar_mensajes('Agregado con exito')
            else:
                self.GUI.mostrar_error('Hubo un error al guardar')
        except Exception as error:
            self.GUI.mostrar_error(f'Error: {error}')

    def cargar_registros(self):
        arreglo = self.services.mostrar_estudiantes()
        self.GUI.cargar_tabla(arreglo)

    def buscar_curso(self):
        try:
            carnet = self.GUI.carnet.get()
            self.GUI.limpiar_tabla()
            arreglo = self.services.buscar_estudiante(carnet)

            self.GUI.cargar_tabla(arreglo)
        except Exception as error:
            self.GUI.mostrar_error(f'Error: {error}')