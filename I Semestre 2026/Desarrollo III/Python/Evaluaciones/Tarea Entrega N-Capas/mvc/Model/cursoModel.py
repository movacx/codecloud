class Curso:
    def __init__(self, codigo_curso, nombre, creditos):
        self.codigo_curso = codigo_curso
        self.nombre = nombre
        self.creditos = creditos

    def to_dict(self):
        return {
            'Codigo': self.codigo_curso,
            'Curso': self.nombre,
            'Creditos': self.creditos
        }

    def __str__(self) -> str:
        return f"{self.codigo_curso}, {self.nombre}, ({self.creditos})"
    