import View.huespedesView as vista            #Vista
import Data.huespedData as manejoHuesped      #Data
from Model.huespedModel import HuespedModel   #Model
class HuespedesController:

    def __init__(self):
        pass

#--------------------------------------------------------------------------------------------------#

    def registrarHuesped(self,nombre,telefono):

        nuevoHuesped = HuespedModel(0,nombre,telefono)
        manejoHuesped.agregarListado(nuevoHuesped)
        return "Agregado con exito!"

#--------------------------------------------------------------------------------------------------#

    def listarHuesped(self):
        mostrar_todos = manejoHuesped.listarTodos()
        if not mostrar_todos:
            vista.mostrarMensaje('No se encontro datos!')
        
        vista.mostrarListados(mostrar_todos)

#--------------------------------------------------------------------------------------------------#

    def buscarHuesped(self, nombre):
        huesped_encontrado = manejoHuesped.searchName(nombre)
        if not huesped_encontrado:
            vista.mostrarMensaje('No se encontro datos!')

        vista.mostrarListados(huesped_encontrado)


        # vista.mostrarListados(huesped_encontrado)

#--------------------------------------------------------------------------------------------------#