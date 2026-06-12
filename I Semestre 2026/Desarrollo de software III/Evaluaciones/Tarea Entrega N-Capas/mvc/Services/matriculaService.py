from Model.matricula import Matricula

class MatriculaService:
    def __init__(self, repo_matricula, repo_estudiante, repo_curso):
        self.repo_matricula = repo_matricula
        self.repo_estudiante = repo_estudiante
        self.repo_curso = repo_curso

    def registro(self, codigo_matricula, carnet_estudiante, codigo_curso, periodo_academico):
        if not codigo_matricula.strip():
            raise ValueError('El campo es obligatorio')
        if not carnet_estudiante.strip():
            raise ValueError('El campo carnet es obligatorio')
        if not codigo_curso.strip():
            raise ValueError('El campo código Curso es obligatorio')
        if not periodo_academico.strip():
            raise ValueError('El campo es obligatorio')

        #==-=-=-=-=-=-Comprobación de existencias=-=-=-=-=-=-=-=-=-=-=-=-=#
        if not self.repo_curso.buscar_por_curso(codigo_curso):
            raise ValueError('No se encontró ningún curso')
        if not self.repo_estudiante.buscar_estudiante(carnet_estudiante):
            raise ValueError('No se encontró ningún estudiante')

        #3. Evitar que se repitan los códigos
        arreglo = self.repo_matricula.buscar_matricula(codigo_matricula)
        if arreglo: #True
            raise ValueError(f'Ya hay una matricula existente con el codigo {codigo_matricula}')

        nueva_matricula = Matricula(codigo_matricula, carnet_estudiante, codigo_curso, periodo_academico)

        exito = self.repo_matricula.agregar(nueva_matricula)
        if exito:
            return True
        else:
            return False

    def mostrar_matriculas(self):
        return self.repo_matricula.mostrar_matriculas()

    def buscar_matricula(self, codigo):
        if not codigo.strip():
            raise ValueError('El carnet es obligatorio')
        return self.repo_matricula.buscar_matricula(codigo)
