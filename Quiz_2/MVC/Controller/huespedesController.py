import View.huespedesView as vista            #Vista
import Data.huespedData as manejoHuesped      #Data
from Model.huespedModel import HuespedModel   #Model
class HuespedesController:

    def __init__(self):
        pass
    
    def registrarHuesped(self,nombre,telefono):

        nuevoHuesped = HuespedModel(0,nombre,telefono)
        manejoHuesped.agregarListado(nuevoHuesped)


    def listarTodos(self):
        
        mostrar_todos = manejoHuesped.listarTodos()
        if not mostrar_todos:
            vista.mostrarMensaje("Eror no se encontraron datos!")
            return
        
        vista.mostrarDatos(mostrar_todos)






    def testeo(self,dato):
        vista.mostrarMensaje(dato)