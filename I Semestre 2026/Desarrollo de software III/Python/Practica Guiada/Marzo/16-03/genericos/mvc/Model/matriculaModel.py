"""Debe contener:
	objeto Estudiante
	objeto Curso
"""

class Matricula:
    def __init__(self, objEstudiante, objCurso):
        self.objEstudiante = objEstudiante
        self.objCurso = objCurso

    def __str__(self):
        return f'{self.objEstudiante} | {self.objCurso}'

