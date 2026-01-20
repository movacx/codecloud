from model.profesorModel import Profesor

class ProfesorController:
    def __init__(self):
        self.lista = []
    
    #------------------Mostrar Datos----------------------------
    def mostrarDatos(self):
        for items in self.lista:
            print(items.mostrarDatos())