class Prestamo:
    def __init__(self, numeroPrestamo, estudianteAsociado, libroAsociado, fecha):
        self.numeroPrestamo = numeroPrestamo
        self.estudianteAsociado = estudianteAsociado
        self.libroAsociado = libroAsociado
        self.fecha = fecha

    def __str__(self):
        return f'{self.numeroPrestamo} | {self.estudianteAsociado} | {self.libroAsociado} | {self.fecha}'