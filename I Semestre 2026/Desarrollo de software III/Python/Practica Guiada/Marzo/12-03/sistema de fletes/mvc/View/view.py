class Vista:
    """vista del sistema"""
    def menu(self):
        print("/n === SISTEMA DE FLETES ===")
        print("1. Agregar Cliente")
        print("2. Agregar Flete")
        print("3. Modificar Cliente")
        print("4. Modificar Flete")
        print("5. Consultar Cliente")
        print("6. Consultar Flete")
        print('0. Salir')
        return int(input('Seleccione una opcion: '))

    def pedir_cliente(self):
        codigo=input('Ingrese el codigo del cliente: ')
        nombre=input('Ingrese el nombre del cliente: ')
        telefono=input('Ingrese el telefono del cliente: ')
        return codigo, nombre, telefono

    def pedir_flete(self):
        numero=input('Ingrese el numero del flete: ')
        destino=input('Ingrese el destino: ')
        monto=input('Ingrese el monto: ')
        indice_cliente=input('Ingrese el indice_cliente: ')

        return numero, destino, monto, indice_cliente

    def mostrar_lista(self, lista):
        if not lista:
            print("No hay datos")
        else:
            for i, obj in enumerate(lista):
                # Usamos f-strings para mostrarlo limpio
                print(f"{i} - {obj}")