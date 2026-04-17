from Model.cursoModel import Curso
from Model.estudianteModel import Estudiante
from Model.matriculaModel import Matricula
from Model.repositorio import Repositorio
from View.vista import Vista


class Controlador:
    def __init__(self):
        self.repo_estudiantes = Repositorio[Estudiante]()
        self.repo_curso = Repositorio[Curso]()
        self.repo_matricula = Repositorio[Matricula]()
        self.vista = Vista()


    def agregar_estudiantes(self, carnet, nombre, carrera):
        estudiante = Estudiante(carnet, nombre, carrera)
        self.repo_estudiantes.agregar(estudiante)


    def agregar_curso(self, sigla, nombreCurso, creditos):
        curso = Curso(sigla, nombreCurso, creditos)
        self.repo_curso.agregar(curso)

    def registrar_matricula(self, sigla, carnet):
        cursoEncontrado = None
        estudianteEncontrado = None

        for items in self.repo_curso.consultar():
            if items.sigla == sigla:
                cursoEncontrado = items
                break

        for items in self.repo_estudiantes.consultar():
            if items.carnet == carnet:
                estudianteEncontrado = items
                break

        if not cursoEncontrado:
            self.vista.mostrar_mensaje('No se encontro el curso ingresado!')
        elif not estudianteEncontrado:
            self.vista.mostrar_mensaje('No se encontro el estudiante ingresado!')
        else:
            registro  = Matricula(estudianteEncontrado, cursoEncontrado)
            self.repo_matricula.agregar(registro)

    def consultar_estudiantes(self):
        self.vista.mostrar_datos(self.repo_estudiantes.consultar())

    def consultar_cursos(self):
        self.vista.mostrar_datos(self.repo_curso.consultar())

    def consultar_matriculas(self):
        self.vista.mostrar_datos(self.repo_matricula.consultar())

    def buscarEstudiante(self, carnet):
        for items in self.repo_estudiantes.consultar():
            if items.carnet == carnet:
                print(items)

