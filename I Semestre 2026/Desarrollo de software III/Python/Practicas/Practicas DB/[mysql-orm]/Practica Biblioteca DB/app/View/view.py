
def menu_autor():
    return int(input('''
        -- Gestión de Autores --
        1. Registrar autor
        2. Listar autores
        3. Buscar autor por ID
        4. Actualizar autor
        5. Eliminar autor
        0. Volver
        '''))

def menu_libro():
    return int(input(('''
        -- Gestión de Libros --
        1. Registrar libro
        2. Listar libros
        3. Buscar libro por código
        4. Actualizar libro
        5. Eliminar libro
        0. Volver
        Opcion: ''')))

def menu_reportes():
    return int(input(('''
        -- Reportes --
        1. Libros ordenados por título
        2. Libros por categoría
        3. Libros por autor
        4. Autores por nacionalidad
        0. Volver
        Opcion: ''')))

def mostrar_datos(dato):
    print(f'{dato}')

def mostrar_mensaje(mensaje):
    print(mensaje)

def menu_principal():
    return int(input('''
        Sistema de Gestión Biblioteca
        1. Gestión de Autores
        2. Gestión de Libros
        3. Reportes
        0. Salir
        Opcion: 
        '''))