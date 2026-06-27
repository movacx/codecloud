import View.view as vista

class ControllerLibro:
    def __init__(self, service_libro):
        self.service_libro = service_libro()

    def registrar_libro(self, codigo,titulo,categoria,anio_publicacion,autor_id):
        try:
            exito = self.service_libro.create_libro(codigo,titulo,categoria,anio_publicacion,autor_id)
            if exito:
                vista.mostrar_mensaje('Registrado correctamente')
        except Exception as error:
            vista.mostrar_mensaje(error)

    def mostrar_libros(self):
        try:
            datos_encontrados  = self.service_libro.get_libros()
            if datos_encontrados:
                vista.mostrar_datos(datos_encontrados)
        except Exception as error:
            vista.mostrar_mensaje(error)

    def buscar_libro(self, codigo):
        try:
            datos_encontrados  = self.service_libro.get_libro_codigo(codigo)
            if datos_encontrados:
                vista.mostrar_datos(datos_encontrados)
        except Exception as error:
            vista.mostrar_mensaje(error)


    def modificar_libro(self, codigo,titulo,categoria,anio_publicacion,autor_id):
        try:
            exito = self.service_libro.update_libro(codigo,titulo,categoria,anio_publicacion,autor_id)
            if exito:
                vista.mostrar_mensaje('Modificado correctamente!')
        except Exception as error:
            vista.mostrar_mensaje(error)

    def eliminar_libro(self, codigo):
        try:
            exito = self.service_libro.delete_libro(codigo)
            if exito:
                vista.mostrar_mensaje('Eliminado correctamente!')
        except Exception as error:
            vista.mostrar_mensaje(error)


    def ordenar_libros(self):
        try:
            encontrado = self.service_libro.ordenar_titulos()
            if encontrado:
                vista.mostrar_datos(encontrado)
        except Exception as error:
            vista.mostrar_mensaje(error)

    # def filtrar_autores(self, nombre_autor):
    #     try:
    #         dato_encontrado = self.service_libro.filtrar_autor_por_libro(nombre_autor)
    #         if dato_encontrado:
    #             vista.mostrar_mensaje(dato_encontrado)
    #     except Exception as error:
    #         vista.mostrar_mensaje(error)

    def filtrar_Categoria(self, categoria):
        try:
            dato_encontrado = self.service_libro.filtrar_categoria_mejorada(categoria)
            if dato_encontrado:
                vista.mostrar_mensaje(dato_encontrado)
        except Exception as error:
            vista.mostrar_mensaje(error)



    def filtrar_autores_por_libro(self, nombre_autor):
        try:
            dato_encontrado = self.service_libro.filtrar_autor_por_libro(nombre_autor)
            if dato_encontrado:
                vista.mostrar_mensaje(dato_encontrado)
        except Exception as error:
            vista.mostrar_mensaje(error)