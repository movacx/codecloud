import View.reservaView as vista
from Model.reservaModel import ReservaModel

class  ReservaController:
    
    def __init__(self):
        pass
    
    def registrarReserva(numero_habitacion, id_huesped, fecha_entrada, fecha_salida):

        nuevaReserva = ReservaModel(numero_habitacion, id_huesped, fecha_entrada, fecha_salida)
        manejoReserva.agregarListado(nuevaReserva)


    def listarTodos():
        
        mostrar_todos = manejoHuesped.listarTodos()
        if not mostrar_todos:
            vista.mostrarMensaje("Eror no se encontraron datos!")
            return
        
        vista.mostrarDatos(mostrar_todos)