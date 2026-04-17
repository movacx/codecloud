
class Matricula:
    def __init__(self, codigo_matricula, carnet_estudiante, codigo_curso, periodo_academico):
        self.codigo_matricula = codigo_matricula
        self.carnet_estudiante = carnet_estudiante
        self.codigo_curso = codigo_curso
        self.periodo_academico = periodo_academico


    def to_dict(self):
        return {
            'Codigo matricula':self.codigo_matricula,
            'Carnet estudiante':self.carnet_estudiante,
            'Codigo curso':self.codigo_curso,
            'Periodo academico':self.periodo_academico
        }

    def __str__(self):
        return self.codigo_matricula, self.carnet_estudiante, self.codigo_curso, self.periodo_academico


