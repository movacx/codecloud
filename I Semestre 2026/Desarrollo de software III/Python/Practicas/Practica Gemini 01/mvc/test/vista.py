class Vista:

    @staticmethod
    def menu() -> int:
        return int(input('''
        1. Agregar un video juego
        2. Consultar todos los juegos
        3. Buscar juego por titulo
        0. Salir
        input: '''))

    @staticmethod
    def pedir_juego() -> tuple:
        titulo = input('Ingrese el titulo: ')
        genero = input('Ingrese el genero: ')
        precio = float(input('Ingrese el precio: '))

        return titulo, genero, precio

    @staticmethod
    def mostrar_juegos(diccionario: list) -> None:
        if not diccionario:
            print('No hay juegos registrados en el sistema')
        else:
            print('\n---Lista de juegos--------')
            for items in diccionario:
                print(items)

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(mensaje)

