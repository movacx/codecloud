import View.view as vista
from Service.service_duenos import ServiceDuenos

class ControllerDueños:
    def __init__(self ):
        self.service_duenos = ServiceDuenos()
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def registrar_dueno(self, nombre,telefono,email):
        try:
            exito = self.service_duenos.registrar_duenos(nombre,telefono,email)
            if exito:
                vista.mostrar_mensajes('Dueño registrado correctamente')
        except Exception as error:
            vista.mostrar_mensajes(error)
        
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def mostrar_duenos(self):
        try:
            datos =  self.service_duenos.listar_duenos()
            vista.mostrar_datos(datos)
        except Exception as error:
            vista.mostrar_mensajes(error)
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def filtrar_duenos(self, nombre):
        try:
            datos = self.service_duenos.buscar_duenos(nombre)
            vista.mostrar_datos(datos)
        except Exception as error:
            vista.mostrar_mensajes(error)

    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def actualizar_datos(self, id,nombre,telefono,email):
        try:
            exito = self.service_duenos.actualizar_duenos(id,nombre,telefono,email)
            if exito:
                vista.mostrar_mensajes('Modificado exitosamente')
        except Exception as error:
            vista.mostrar_mensajes(error)

    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def eliminar_dato(self, id):
        try:
            exito = self.service_duenos.eliminar(id)
            if exito:
                vista.mostrar_mensajes('eliminar exitosamente')
        except Exception as error:
            vista.mostrar_mensajes(error)