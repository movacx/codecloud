class Prestamo:
    def __init__(self, numeroPrestamo, estudianteAsociado, libroAsociado, fecha):
        self.numeroPrestamo = numeroPrestamo
        self.estudianteAsociado = estudianteAsociado
        self.libroAsociado = libroAsociado
        self.fecha = fecha
    def __str__(self):
        return f"""
Numero de prestamo: {self.numeroPrestamo}
Estudiante Asociado: {self.estudianteAsociado}
Libro asociado al estudiante: {self.libroAsociado}
Fecha del prestamo: {self.fecha}"""