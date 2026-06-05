"""
    Esta capa se encarga de comunicarse con la base de datos
    Aca se realizan las consultas sql
    INSERT
    SELECT
    UPDATE
    DELETE
"""

from database.conexion import obtener_conexion
from model.estudiante import Estudiante


class EstudianteRepository:

    def __init__(self):
        pass

    def registrar(self, estudiante):
        """
        Registra un estudiante en la base de datos
        """

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO estudiante (nombre, correo, carrera)
        VALUES (%s, %s, %s)
        """

        valores = (
            estudiante.nombre,
            estudiante.correo,
            estudiante.carrera
        )

        cursor.execute(sql, valores)

        conexion.commit()

        cursor.close()
        conexion.close()

        return True

    def consultar_todos(self):

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = 'SELECT id, nombre, correo, carrera FROM estudiante'

        cursor.execute(sql)

        registros = cursor.fetchall()

        estudiantes = []   # 👈 ESTA es la lista correcta

        for registro in registros:

            estudiante = Estudiante(
                id_estudiante=registro[0],
                nombre=registro[1],
                correo=registro[2],
                carrera=registro[3]
            )

            estudiantes.append(estudiante)   # 👈 aquí se usa la lista

        cursor.close()
        conexion.close()

        return estudiantes

    def busacar_por_id(self, id_estudiante):
        '''
        Busca un estudiante por ID
        '''

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = '''
        SELECT id, nombre, correo, carrera
        FROM estudiante
        WHERE id=%s
        '''

        cursor.execute(sql, (id_estudiante,))

        registro = cursor.fetchone()

        cursor.close()
        conexion.close()

        if registro is None:
            return None

        return Estudiante(
            id_estudiante=registro[0],
            nombre=registro[1],
            correo=registro[2],
            carrera=registro[3]
        )

    def actualizar(self, estudiante):
        '''
        Actualiza un estudiante existente
        '''

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = '''
        UPDATE estudiante
        SET nombre=%s,
            correo=%s,
            carrera=%s
        WHERE id=%s
        '''

        valores = (
            estudiante.nombre,
            estudiante.correo,
            estudiante.carrera,
            estudiante.id_estudiante
        )

        cursor.execute(sql, valores)

        conexion.commit()

        filas_afectadas = cursor.rowcount

        cursor.close()
        conexion.close()

        return filas_afectadas > 0

    def eliminar(self, id_estudiante):

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = 'DELETE FROM estudiante WHERE id=%s'

        cursor.execute(sql, (id_estudiante,))

        conexion.commit()

        filas_afectadas = cursor.rowcount

        cursor.close()
        conexion.close()

        return filas_afectadas > 0

    def existe_correo(self, correo):
        '''
        Verifica si ya existe un correo
        '''

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = 'SELECT id FROM estudiante WHERE correo=%s'

        cursor.execute(sql, (correo,))

        registro = cursor.fetchone()

        cursor.close()
        conexion.close()

        return registro is not None