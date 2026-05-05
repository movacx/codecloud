from Model.cursoModel import Curso

class CursoService:
    def __init__(self, repo):
        self.repo = repo

    def registro_curso(self, codigo_curso, nombre, creditos):

        if not codigo_curso.strip():
            raise ValueError('El codigo de curso es obligatorio')
        if not nombre.strip():
            raise ValueError('El nombre es obligatorio')
        if creditos <= 0:
            raise ValueError('El campo de créditos debe ser superior a 0')

        #=-=-=-=-=- Validar que no se repita el codigo del curso =-=-=-=-=-
        if self.buscar_por_codigo(codigo_curso):
            raise ValueError('El codigo del curso ya existe, ingrese otro valor')

        nuevo_curso = Curso(codigo_curso, nombre, creditos)
        exito = self.repo.guardar(nuevo_curso)
        if exito:
            return True
        else:
            return False

    def mostrar_cursos(self):
        return self.repo.obtener_todos()

    def buscar_por_codigo(self, codigo_curso):
        if not codigo_curso.strip():
            raise ValueError('El código de curso es obligatorio')
        return self.repo.buscar_por_curso(codigo_curso)
