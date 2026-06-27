import View.view as vista

class EstudianteController:
    def __init__(self,Estudiante_service):
        self.service_estudiante = Estudiante_service

    def registrar_estudiante(self, id, nombre, correo, carrera):
        try:
            estudiante = self.service_estudiante.guardar(id, nombre, correo, carrera)
            if estudiante:
                vista.mostrar_mensaje("Agregado correctamente")
            return estudiante

        except Exception as Error:
            return vista.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def mostrar_estudiantes(self):
        try:
            estudiante = self.service_estudiante.listar()
            if estudiante:
                vista.mostrar_dato(estudiante)

        except Exception as Error:
            return vista.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def buscar_estudiante(self, id):
        try:
            encontrado = self.service_estudiante.buscar_id(id)
            if encontrado:
                vista.mostrar_dato(encontrado)

        except Exception as Error:
            return vista.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def actualizar_estudiante(self, id, nombre, correo, carrera):
        try:
            encontrado = self.service_estudiante.actualizar(id, nombre, correo, carrera)
            if encontrado:
                vista.mostrar_mensaje("Modificado correctamente")

        except Exception as Error:
            return vista.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def eliminar_estudiante(self, id):
        try:
            encontrado = self.service_estudiante.eliminar(id)
            if encontrado:
                vista.mostrar_mensaje("Eliminado correctamente")

        except Exception as Error:
            return vista.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------