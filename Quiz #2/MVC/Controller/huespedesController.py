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
            return vista.fileNoFound()
        
        vista.mostrarListados(mostrar_todos)

#--------------------------------------------------------------------------------------------------#

    def buscarHuesped(self, nombre):
        huesped_encontrado = manejoHuesped.searchName(nombre)
        if not huesped_encontrado:
            return vista.fileNoFound()
        

        vista.mostrarListados(huesped_encontrado)


#--------------------------------------------------------------------------------------------------#
    def buscarId(self, id):
        huesped_id = manejoHuesped.searchId(id)

        if not huesped_id:
            return vista.fileNoFound()
        
        vista.mostrarListados(huesped_id)
        
#--------------------------------------------------------------------------------------------------#
   
    def modificarHuesped(self, id,nombre,telefono):
        nuevoObjeto = HuespedModel(id,nombre,telefono)
        
        modificarHuesped = manejoHuesped.modificarLista(id,nuevoObjeto)
        
        if not modificarHuesped:
            return vista.fileNoFound()
        
        if modificarHuesped == True:
            vista.mostrarMensaje('Modificado con exito!')
        else:
            vista.mostrarMensaje('Id no encontrado!')
            
#--------------------------------------------------------------------------------------------------#
        
    def eliminarHuesped(self, id):
        eliminarObjeto = manejoHuesped.eliminarLista(id)
        
        if not eliminarObjeto:
            return vista.fileNoFound()
        
        if eliminarObjeto:
            vista.mostrarMensaje('Eliminado con exito!')
        else:
            vista.mostrarMensaje('No se encontro Id!')
        
        
    
    
    

		