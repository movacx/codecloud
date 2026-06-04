

from Model.libro_model import Libro

class BibliotecaRepository:
    def __init__(self, conexion):
        self.obtener_conexion = conexion

    # -=-==--=-==-=--==-=-=-=-=-==-=--==--==--=-=-==-=--==-=--==-=-=-=-=-=-=--==-=-=-=-=-=--=#
    def registrar(self, obj_libro):
        conexion = self.obtener_conexion
        cursor = self.obtener_conexion.cursor

        sql = '''
            INSERT INTO libros(codigo,titulo,autor,categoria)
            VALUES(%s,%s,%s,%s)
        '''

        valores = (obj_libro.codigo,
                   obj_libro.titulo,
                   obj_libro.autor,
                   obj_libro.categoria)

        cursor.execute(sql, valores)

        conexion.commit()

        cursor.close()
        conexion.close()

        return True

    #-=-==--=-==-=--==-=-=-=-=-==-=--==--==--=-=-==-=--==-=--==-=-=-=-=-=-=--==-=-=-=-=-=--=#

    def consultar_datos(self):
        conexion = self.obtener_conexion
        cursor = self.obtener_conexion.cursor

        sql = '''
            SELECT *
            FROM libros
        '''

        cursor.execute(sql)
        registros = cursor.fetchall()

        lista_libros = []

        for items in registros:
            nuevo_libro = Libro(
                codigo = items[0],
                titulo = items[1],
                autor = items[2],
                categoria = items[3]
            )

            lista_libros.append(nuevo_libro)

        cursor.close()
        conexion.close()

        return lista_libros

    # -=-==--=-==-=--==-=-=-=-=-==-=--==--==--=-=-==-=--==-=--==-=-=-=-=-=-=--==-=-=-=-=-=--=#









