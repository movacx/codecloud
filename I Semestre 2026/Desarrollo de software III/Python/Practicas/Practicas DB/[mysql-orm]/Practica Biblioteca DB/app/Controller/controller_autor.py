import  View.view as vista
class ControllerAutor:
    def __init__(self, service):
        self.service = service()

    def registrar_autor(self, nombre,nacionalidad):
        try:
            exito = self.service.create_autor(nombre,nacionalidad)
    
            exito, autor = self.service.create_autor(nombre, nacionalidad)
            if exito:
                vista.mostrar_mensaje(f'Se registro: {autor}')

        except Exception as error:
            vista.mostrar_mensaje(error)

    def listar_autores(self):
        try:
            return self.service.list_all()
        except Exception as error:
            vista.mostrar_mensaje(error)

    def buscar_autor(self, id):
        try:
            dato_encontrado = self.service.get_autor(id)
            if dato_encontrado:
                return dato_encontrado
        except Exception as error:
            vista.mostrar_mensaje(error)

    def modificar_autor(self, id, nombre, nacionalidad):
        try:
            exito = self.service.update_autor(id, nombre, nacionalidad)
            if exito:
                vista.mostrar_mensaje('Modificado correctamente')
        except Exception as error:
            vista.mostrar_mensaje(error)

    def eliminar_autor(self, id):
        try:
            exito = self.service.delete_autor(id)
            if exito:
                vista.mostrar_mensaje('Eliminado correctamente')
        except Exception as error:
            vista.mostrar_mensaje(error)

    def buscar_autor_por_nombre(self, nombre):
        try:
            encontrado = self.service.buscar_nombre(nombre)
            if encontrado:
                vista.mostrar_mensaje(encontrado)
        except Exception as error:
            vista.mostrar_mensaje(error)

    def filtrar_autor_por_nacionalidad(self, nacionalidad):
        try:
            dato = self.service.filtrar_nacionalidad(nacionalidad)
            if dato:
                vista.mostrar_datos(dato)
        except Exception as error:
            vista.mostrar_mensaje(error)
