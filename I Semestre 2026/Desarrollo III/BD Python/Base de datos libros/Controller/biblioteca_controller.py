from View.interfaz_biblioteca import ViewBiblioteca

class BibliotecaController:
    def __init__(self, service_biblioteca):
        self.service_biblioteca = service_biblioteca
        self.interfaz = ViewBiblioteca()

    def cargar_interfaz(self):
        while True:

            opcion =  self.interfaz.mostrar_menu()

            if opcion == 1:
                datos = self.interfaz.pedir_datos()
                self.interfaz.mostrar_mensaje(self.service_biblioteca.registrar_libro(*datos))

            elif opcion == 2:
                self.interfaz.mostrar_mensaje(self.service_biblioteca.consultar_libros())

            elif opcion == 3:
                self.interfaz.mostrar_mensaje(self.service_biblioteca.buscar_libro(self.buscar_por_codigo()))

            elif opcion == 4:
                self.interfaz.mostrar_mensaje(self.service_biblioteca.buscar_categoria(self.buscar_por_categoria()))

            elif opcion == 7:
                break

    def buscar_por_codigo(self):
        codigo = self.interfaz.pedir_codigo()
        return codigo
        
    def buscar_por_categoria(self):
        categoria = self.interfaz.pedir_categoria()
        return categoria

