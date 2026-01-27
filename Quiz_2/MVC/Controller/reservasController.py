import View.reservaView as vista
from Model.reservaModel import ReservaModel

class  ReservaController:
    
    def __init__(self):
        pass
    
    def registrarReserva(nombre,telefono):

        nuevaReserva = ReservaModelModel(0,nombre,telefono)
        manejoReserva.agregarListado(nuevaReserva)


    def listarTodos():
        
        mostrar_todos = manejoHuesped.listarTodos()
        if not mostrar_todos:
            vista.mostrarMensaje("Eror no se encontraron datos!")
            return
        
        vista.mostrarDatos(mostrar_todos)