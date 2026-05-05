from View.matriculaView import MatriculaGUI

#Services
from Services.matriculaService import MatriculaService
from Services.estudianteService import EstudianteService
from Services.cursoService import CursoService

class MatriculaController:
    def __init__(self, root, services):
        self.service = services
        self.GUI = MatriculaGUI(root, self)
        self.cargar_registros()
    def registrar_matricula(self):
        try:
            codigo_matricula = self.GUI.codigo_matricula.get()
            carnet_estudiante = self.GUI.carnet_estudiante.get()
            codigo_curso = self.GUI.codigo_curso.get()
            periodo_academico = self.GUI.periodo_academico.get()

            exito = self.service.registro(codigo_matricula, carnet_estudiante, codigo_curso, periodo_academico)
            if exito:
                self.GUI.mostrar_mensajes('Agregado con éxito')
            else:
                self.GUI.mostrar_error('Hubo un error al guardar')
        except Exception as error:
            self.GUI.mostrar_mensajes(f'{error}')

    def cargar_registros(self):
        arreglo = self.service.mostrar_matriculas()
        self.GUI.cargar_tabla(arreglo)

    def buscar_curso(self):
        try:
            codigo_matricula = self.GUI.codigo_matricula.get()
            self.GUI.limpiar_tabla()
            arreglo = self.service.buscar_matricula(codigo_matricula)

            self.GUI.cargar_tabla(arreglo)
        except Exception as error:
            self.GUI.mostrar_mensajes(f'{error}')
