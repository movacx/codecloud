from View.cursoView import CursoGUI

class CursoController:
    def __init__(self, root, services):
        self.GUI = CursoGUI(root, self)
        self.services = services
        self.cargar_registros()

    def registrar_curso(self):
        try:
            codigo = self.GUI.codigo.get()
            nombre = self.GUI.nombre.get()
            creditos = self.GUI.creditos.get()

            exito = self.services.registro_curso(codigo, nombre, int(creditos))
            if exito:
                self.GUI.mostrar_mensajes('Agregado con exito')
            else:
                self.GUI.mostrar_error('Hubo un error al guardar')
        except Exception as error:
            self.GUI.mostrar_error(f'Error {error}')


    def cargar_registros(self):
        try:
            arreglo = self.services.mostrar_cursos()
            self.GUI.cargar_tabla(arreglo)
        except Exception as error:
            self.GUI.mostrar_error(f'Error {error}')


    def buscar_curso(self):
        try:
            codigo = self.GUI.codigo.get()
            self.GUI.limpiar_tabla()
            arreglo = self.services.buscar_por_codigo(codigo)

            self.GUI.cargar_tabla(arreglo)
        except Exception as error:
            self.GUI.mostrar_error(f'Error {error}')
