"""Debe contener:
	sigla (ej: IF0006)
	nombre del curso
	créditos
"""

class Curso:
    def __init__(self, sigla, nombreCurso, creditos):
        self.sigla = sigla
        self.nombreCurso = nombreCurso
        self.creditos = creditos

    def __str__(self):
        return f"{self.sigla} | {self.nombreCurso} | {self.creditos}"
    