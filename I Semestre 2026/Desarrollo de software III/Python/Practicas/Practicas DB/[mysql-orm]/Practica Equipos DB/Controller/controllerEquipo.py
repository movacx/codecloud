
import View.view as view
class EquipoController:
    def __init__(self,service):
        self.service_equipo = service

    def guardar_equipo(self, codigo, nombre, marca, estado, categoria_id):
        try:
            team = self.service_equipo.guardar(codigo, nombre, marca, estado, categoria_id)
            if team:
                view.mostrar_mensaje("Agregado correctamente")
            return team

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def mostrar_equipos(self):
        try:
            equipo = self.service_equipo.listar()
            if equipo:
                view.mostrar_dato(equipo)

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def buscar_equipos(self, codigo):
        try:
            encontrado = self.service_equipo.buscar_id(codigo)
            if encontrado:
                view.mostrar_dato(encontrado)

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def actualizar_equipos(self, codigo, nombre, marca, estado, categoria_id):
        try:
            encontrado = self.service_equipo.actualizar(codigo,nombre, marca, estado, categoria_id)
            if encontrado:
                view.mostrar_mensaje("Modificado correctamente")

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def eliminar_equipos(self, codigo):
        try:
            encontrado = self.service_equipo.eliminar(codigo)
            if encontrado:
                view.mostrar_mensaje("Eliminado correctamente")

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------