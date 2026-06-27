
import View.view as vista

class CategoriaController:
    def __init__(self, service):
        self.service_categoria = service

    def guardar_categoria(self, id, nombre):
        try:
            exito = self.service_categoria.guardar(id, nombre)
            if exito:
                vista.mostrar_mensaje('registrado correctamente!')

        except Exception as Error:
            vista.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def mostrar_categorias(self):
        try:
            dato = self.service_categoria.listar()
            vista.mostrar_dato(dato)

        except Exception as Error:
            vista.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def buscar_categoria(self, id):
        try:
            datos = self.service_categoria.buscar_id(id)
            vista.mostrar_dato(datos)
        except Exception as Error:
            vista.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def actualizar_categoria(self, id, nombre):
        try:
            encontrado = self.service_categoria.actualizar(id)

            if encontrado is not None:
                self.service_categoria.update_categoria(id, nombre)
                vista.mostrar_mensaje("Modificado correctamente")

        except Exception as Error:
            vista.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def eliminar_categoria(self, id):
        try:
            encontrado = self.service_categoria.delete_categoria(id)
            if encontrado:
                vista.mostrar_mensaje("Eliminado correctamente")
                
        except Exception as Error:
            vista.mostrar_mensaje(Error)

