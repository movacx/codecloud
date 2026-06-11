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
        1. Registrar periferico: 
        2. Ver perifericos:
        3. Buscar periferico por modelo: 
        input: '''))

    @staticmethod
    def pedir_datos():
        modelo = input('Ingrese el modelo del periferico: ')
        tipo = input('Ingrese el tipo de periferico: ')
        precio = float(input('Ingrese el precio del periferico: '))
        return modelo, tipo, precio

    @staticmethod
    def pedir_modelo():
        return input('Ingrese el modelo del periferico: ')
