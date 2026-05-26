"""
    Esta capa se encarga de comunicarse con la base de datos
    Aca se realizan las consultas sql
    INSERT
    SELECT
    UPDATE
    DELETE

    ACA
"""
from database.conexion import obtener_conexion
from model.estudiante import Estudiante
from database.conexion import mysql

class EstudianteRepository:
    def __init__(self,estudiante):
        """
        Registra un estudiante en la base de datos
        estudiante: Objeto de tipo estudiante
        return un boolean indicando verdadero si el registro es exitoso
        """

        #Se obtiene la conexion a la base de datos
        conexion = obtener_conexion()

        #el cursor permite ejecutar
        cursor = conexion.cursor()

        #consulta sql parametrizada
        #se usa %s para evitar concatenar
        #datos(nombres de variables) en sql

        sql = """
        INSERT INTO estudiantes (nombre,correo,carrera)
        VALUES(%s, %s, %s)
        """

        #tupla con los valores que reemplazaran
        #los %s en la consulta

        valores = (estudiante.nombre, estudiante.correo, estudiante.carrera)

        #Ejecuta la consulta con sus valores
        cursor.execute(sql, valores)

        #confirma los cacmbios en la base de datos
        conexion.commit()
        #Se cierrra el cursor y la conexion para liberar recursos
        cursor.close()
        conexion.close()
        return True
    
    def consultar_todos(self):
        conexion = obtener_conexion()

        #el cursor permite ejecutar
        cursor = conexion.cursor()
        cursor.execute('SELECT id, nombre, correo, carrera FROM estudiante')

        #El metodo fetchall obteien todos los registros registrados
        registros = cursor.fetchall()

        #Lista donde se almacenaran los objetos estudiante
        estudiantes = []

        #se recorre cada registro devuelto por la base de datos

        for registro in registros:
            #cada registro es una tupla con el orden
            #id, nombre, correo, carrera
            estudiantes=estudiantes(
                id_estudiante=registro[0],
                nombre=registro[1],
                correo=registro[2],
                carrera=registro[3]
            )

            #Se registra el objeto estudiante a la lista

            estudiantes.append(estudiante)
        cursor.close()
        conexion.close()
        return estudiantes
    
    def busacar_por_id(self, id_estudiante):
        '''
        Busca un estudiante por su ID
        
        :param self: id_estudiante: ID del estudiante que se buscara
        Si existe el objeto con el id dato se retorna
        '''

        #Se obtiene la conexion a la base de dato
        conexion = obtener_conexion()

        #el cursor permite ajecutar las instrucciones SQL
        cursor = conexion.cursor()
        
        #Consulta con Where para filtrar por ID

        sql = 'SELECT id, nombre,correo, FROM estudiante WHERE id=%s'

        cursor.execute(sql,(id_estudiante))

        #fetchone obtiene un solo registro
        registro=cursor.fetchone()

        cursor.close()
        conexion.close()

        #Si no se encuentra un estudiante
        if registro is None: 
            return None

        #Si se encontro, se convierte en un objeto
        #Estudiante y se devuelve
        return Estudiante(
            id_estudiante=registro[0],
            nombre=registro[1],
            correo=registro[2],
            carrera=registro[3]
        
        )
    
    def actualizar(self, estudiante):
        '''
        Actualiza los datos de un estudiante exisstente
        Estudiante: Objeto estudiante con el id y los nuevos datos
        return True si los 
        '''

        #Se obtiene la conexion a la base de dato
        conexion = obtener_conexion()

        #el cursor permite ajecutar las instrucciones SQL
        cursor = conexion.cursor()

        sql = '''
        UPDATE estudiante
        SET nombre=%s,
            correo=%s,
            carrera=%s,
        WHERE id=%s
    '''
        
        valores = (
            estudiante.correo,
            estudiante.carrera,
            estudiante.id_estudiante
        )

        cursor.execute(sql, valores)
        conexion.commit()

        #rowcount indica cuantas filas fueron afectadas por la consulta
        filas_afectadas = cursor.rowcount

        cursor.close()
        conexion.close()

        return filas_afectadas > 0
    
    def eliminar(self, id_estudiante):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = 'DELETE FROM estudiantes WHERE id=%s'

        cursor.execute(sql,(id_estudiante))
        conexion.commit()

        #rowcount indica cuantas filas fueron afectadas
        filas_afectadas = cursor.rowcount
        cursor.close()
        conexion.close()
        return filas_afectadas > 0
    
    def existe_correo(self, correo):
        'Verifica si existe un estudiante con el correo indicado, '
        'correo indicado correo que se desea validar true si el correo existe o false en caso contrario'
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = 'SELECT id FROM estudiante WHERE correo=%s'
        cursor.execute(sql,(correo,))
        registro=cursor.fetchone()

        cursor.close()
        conexion.close()

        return registro is not None
    


