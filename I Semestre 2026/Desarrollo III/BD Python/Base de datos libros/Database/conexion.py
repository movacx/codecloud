import mysql.connector
from mysql.connector import Error

class DataBaseConection:
    def obtener_conexion(self):
        try:

            conexion = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'Skull_fab@19',
                database = 'Biblioteca',
                port = 3306
            )
            return conexion

        except Error as error:
            print('Error al intentar conectar con la base de datos', error)
            raise
