class Vista:

    @staticmethod
    def imprimir_datos(diccionario):
        if not diccionario:
            print('No se encontraron datos')
        else:
            for items in diccionario:
                print(items)

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)

    @staticmethod
    def mostrar_menu():
        return int(input('''
        1. Registrar Platillo: 
        2. Ver Platillos:
        3. Buscar Platillo por nombre: 
        input: '''))

    @staticmethod
    def pedir_datos():
        nombre = input('Ingrese el nombre del platillo: ')
        precio = float(input('Ingrese el precio del platillo: '))
        categoria = input('Ingrese la categoria del platillo: ')
        return nombre, precio, categoria

    @staticmethod
    def pedir_nombre():
        return input('Ingrese el nombre del platillo: ')
