

from Model.libro_model import Libro

class BibliotecaRepository:
    def __init__(self, conexion):
        self.database = conexion

    # -=-==--=-==-=--==-=-=-=-=-==-=--==--==--=-=-==-=--==-=--==-=-=-=-=-=-=--==-=-=-=-=-=--=#
    def registrar(self, obj_libro):
        conexion = self.database.obtener_conexion()
        cursor = conexion.cursor()

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
        conexion = self.database.obtener_conexion()
        cursor = conexion.cursor()

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

    def consultar_libro(self, codigo):
        conexion = self.database.obtener_conexion()
        cursor = conexion.cursor()

        sql = '''
            SELECT *
            FROM libros
            WHERE codigo=%s
        '''

        cursor.execute(sql, (codigo,))
        registro = cursor.fetchall()

        cursor.close()
        conexion.close()

        if registro is None:
            return None
        
        lista_libros = []

        for items in registro:
            lista_libros.append(items)


        return lista_libros
    # -=-==--=-==-=--==-=-=-=-=-==-=--==--==--=-=-==-=--==-=--==-=-=-=-=-=-=--==-=-=-=-=-=--=#

    def filtrar_categoria(self, categoria):
        resultado = []

        conexion = self.database.obtener_conexion()
        cursor = conexion.cursor()

        sql = '''
            SELECT *
            FROM libros
            where categoria=%s
        '''

        cursor.execute(sql, (categoria,))
        
        registro = cursor.fetchone()

        cursor.close()
        conexion.close()

        for items in registro:
            resultado.append(items)

        return resultado


    # -=-==--=-==-=--==-=-=-=-=-==-=--==--==--=-=-==-=--==-=--==-=-=-=-=-=-=--==-=-=-=-=-=--=#

    def actualizar_datos(self, obj_libro):
        conexion = self.database.obtener_conexion()
        cursor = conexion.cursor()

        sql = '''
            UPDATE libros
            SET codigo=%s,
                titulo=%s,
                autor=%s,
                categoria=%s
            WHERE codigo=%s
        '''

        valores = (
            obj_libro.codigo,
            obj_libro.titulo,
            obj_libro.autor,
            obj_libro.categoria,
            obj_libro.codigo  
        )

        cursor.execute(sql, valores)
        conexion.commit()

        filas_afectadas = cursor.rowcount

        cursor.close()
        conexion.close()

        return filas_afectadas > 0
    
    # -=-==--=-==-=--==-=-=-=-=-==-=--==--==--=-=-==-=--==-=--==-=-=-=-=-=-=--==-=-=-=-=-=--=#

    def eliminar(self, codigo):
        conexion = self.database.obtener_conexion()
        cursor = conexion.cursor()

        sql = '''
            DELETE FROM libros
            WHERE codigo=%s
        '''

        cursor.execute(sql, (codigo,))

        conexion.commit()
        
        filas_afectadas = cursor.rowcount
        cursor.close()
        conexion.close()

        return filas_afectadas>0
    
    