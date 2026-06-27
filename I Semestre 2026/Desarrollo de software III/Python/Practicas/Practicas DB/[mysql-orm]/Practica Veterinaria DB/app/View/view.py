def menu_duenos():
    return int(input('''
            1. Registrar dueño
            2. Listar Dueños
            3. Buscar Dueño por nombre
            4. Actualiza datos
            5. Eliminar
            input: '''))


def menu_mascostas():
    return int(input('''
            1. Registrar mascosta
            2. Listar Mascotas
            3. Buscar mascota por codigo
            4. Actualizar datos
            5. Eliminar mascota
            input: '''))


def menu_principal():
    return int(input('''
            1. Dueños
            2. Mascotas
            input: '''))


def mostrar_mensajes(mensaje):
    print(mensaje)

def mostrar_datos(dato):
    print(f'{dato}')