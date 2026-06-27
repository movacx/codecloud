import View.view as vista
from Service.service_mascotas import ServiceMascota
class ControllerMascota:
    def __init__(self):
        self.service_mascota = ServiceMascota()
    
    def registrar_mascota(self, codigo,nombre,especie,edad,dueno_id):
        # try:
            nuevo_registro = self.service_mascota.registrar_mascota(codigo,nombre,especie,edad,dueno_id)
            if nuevo_registro:
                vista.mostrar_mensajes('Registrado correctamente')
            else:
                vista.mostrar_mensajes('No se pudo registrar')
        # except Exception as error:
        #     vista.mostrar_mensajes(error)

    def mostrar_mascotas(self):
        try:
            datos_encontrados = self.service_mascota.listrar_mascotas()
            if datos_encontrados:
                vista.mostrar_datos(datos_encontrados)
            else:
                vista.mostrar_mensajes('Hubo un error')
        except Exception as error:
            vista.mostrar_mensajes(error)

    def buscar_mascostas(self, codigo):
        try:
            datos_encontrados = self.service_mascota.buscar_mascotas(codigo)
            if datos_encontrados:
                vista.mostrar_datos(datos_encontrados)
            else:
                vista.mostrar_mensajes('Hubo un error')
        except Exception as error:
            vista.mostrar_mensajes(error)

    def actualizar_datos(self, codigo,nombre,especie,edad,dueno_id):
        try:
            exito = self.service_mascota.actualizar_mascota(codigo,nombre,especie,edad,dueno_id)
            if exito:
                vista.mostrar_datos('Actualizado correctamente!')
        except Exception as error:
            vista.mostrar_mensajes(error)

    def eliminar_mascota(self, codigo):
        try:
            exito = self.service_mascota.eliminar()
            if exito:
                vista.mostrar_mensajes('Eliminado correctamente')
        except Exception as error:
            vista.mostrar_mensajes(error)