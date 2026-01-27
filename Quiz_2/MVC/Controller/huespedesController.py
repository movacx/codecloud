import View.huespedesView as vista
import Data.huespedData as manejoHuesped
from Model.huespedModel import HuespedModel
class HuespedesController:

    def __init__(self):
        pass
    
    def registrarHuesped(nombre,telefono):

        nuevoHuesped = HuespedModel(0,nombre,telefono)
        manejoHuesped.agregarListado(nuevoHuesped)


    def listarTodos():
        
        mostrar_todos = manejoHuesped.listarTodos()
        if not mostrar_todos:
            vista.mostrarMensaje("Eror no se encontraron datos!")
            return
        
        vista.mostrarDatos(mostrar_todos)






    def testeo(self,dato):
        vista.mostrarMensaje(dato)