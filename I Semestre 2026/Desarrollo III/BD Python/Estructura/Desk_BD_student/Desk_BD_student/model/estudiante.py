"""
Archivo: estudiante.py

Responsabilidad:
Representa la entidad Estudiante del sistema.

Una entidad es una clase que modela un objeto importante del negocio.
En este caso, un estudiante tiene id, nombre, correo y carrera.
"""


class Estudiante:
    """
    Clase que representa un estudiante.
    """

    def __init__(self, id_estudiante=None, nombre="", correo="", carrera=""):
        """
        Constructor de la clase Estudiante.

        Args:
            id_estudiante: identificador único del estudiante en la base de datos.
            nombre: nombre completo del estudiante.
            correo: correo electrónico del estudiante.
            carrera: carrera a la que pertenece el estudiante.
        """

        # El ID puede ser None cuando el estudiante todavía no ha sido guardado.
        self.id_estudiante = id_estudiante

        # Nombre completo del estudiante.
        self.nombre = nombre

        # Correo electrónico del estudiante.
        self.correo = correo

        # Carrera del estudiante.
        self.carrera = carrera

    def __str__(self):
        """
        Devuelve una representación en texto del estudiante.

        Esto permite imprimir un objeto Estudiante de forma legible.
        """

        return f"ID: {self.id_estudiante} | Nombre: {self.nombre} | Correo: {self.correo} | Carrera: {self.carrera}"
