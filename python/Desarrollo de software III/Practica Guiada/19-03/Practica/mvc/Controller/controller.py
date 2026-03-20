from Model.estudianteModel import Estudiante
from Model.libroModel import Libro
from Model.prestamoModel import Prestamo
from Model.repositorio import Repositorio
from View.vista import Vista

class Controller:
    def __init__(self):
        self.repo_estudiante = Repositorio()
        self.repo_libro = Repositorio()
        self.repo_prestamo = Repositorio()
        self.vista = Vista()

    #Estudiante ---------------------------------------------------------------------------
    def registrar_estudiante(self, carnet, nombre, carrera):
        tupla = (nombre, carrera)
        self.repo_estudiante.agregarEstudiantes(carnet, tupla)

    def consultar_estudiante(self):
        diccionario = self.repo_estudiante.consultarEstudiantes()
        for clave, valor in diccionario.items():
            self.vista.mostrar_datos(f"{clave} : {valor}")

    #Libro ---------------------------------------------------------------------------
    def registrar_libro(self, codigoLibro, titulo, autor, categoria):
        nuevo_libro = Libro(codigoLibro, titulo, autor, categoria)
        self.repo_libro.agregarLibros(codigoLibro, nuevo_libro)

    def consultar_libros(self):
        for clave, valor in self.repo_libro.consultarLibros().items():
            self.vista.mostrar_datos(f"{clave} : {valor}")

    #Prestamo ---------------------------------------------------------------------------
    def registrar_prestamo(self, codigoPrestamo, carnet, codigoLibro, fecha):
        diccionario_estudiantes = self.repo_estudiante.consultarEstudiantes()
        diccionario_libros = self.repo_libro.consultarLibros()

        if carnet not in diccionario_estudiantes:
            self.vista.mostrar_mensaje(f'No se encontro estudiante con el carne: {carnet}')
            return

        if codigoLibro not in self.repo_libro.consultarLibros():
            self.vista.mostrar_mensaje(f'No se encontro libro con el codigo: {codigoLibro}')
            return

        prestamo = (carnet, codigoLibro, fecha)
        self.repo_prestamo.agregarPrestamos(codigoPrestamo, prestamo)

    def consultar_prestamos(self):
        for clave, valor in self.repo_prestamo.consultarPrestamos().items():
            self.vista.mostrar_datos(f"{clave} : {valor}")


    #Categorias ---------------------------------------------------------------------------
    def consultar_categorias(self):
        arreglo = []
        for clave, libro in self.repo_libro.consultarLibros().items():
            arreglo.append(libro.categoria)

        self.vista.mostrar_datos(f'Categirias encontradas: {arreglo}')
