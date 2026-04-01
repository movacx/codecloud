from Model.estudianteModel import Estudiante
from Model.Data.base import BaseEstudiantes

class Controller:
    def __init__(self):
        self.contador = 0
        self.base = BaseEstudiantes()


    def agregarEstudiante(self, carnet, nombre, apellido, carrera):


        # id = self.base.validarUltimoId()
        # print('Id actual: ', id)



        newRegistro = Estudiante(0, carnet, nombre, apellido, carrera)
        completado = self.base.registrar(newRegistro)
    
        if completado:
            print('Guardado en el csv')
        else:
            print('Error al registrar')


    def listar(self):
        
        arregloRecibido = self.base.listar()

        for items in arregloRecibido:
            print(items)
