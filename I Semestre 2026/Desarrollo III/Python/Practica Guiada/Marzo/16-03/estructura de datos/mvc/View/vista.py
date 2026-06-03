class Vista:
    """
    vista del sistema (MVC)
    Encargada unicamente de la interaccin con el usuario
    """
    def menu(self):
        print("/n === SISTEMA DE FLETES ===")
        print("1. Agregar Cliente")
        print("2. Agregar Flete")
        print("3. Consultar Cliente")
        print("4. Consultar Flete")
        print('0. Salir')
        return int(input('Seleccione una opcion: '))

    def pedir_cliente(self):
        codigo=input('Codigo: ')
        nombre=input('Nombre: ')
        telefono=input('Telefono: ')
        return codigo, nombre, telefono

    def pedir_flete(self):
        numero=input('Numero: ')
        destino=input('Destino: ')
        monto=input('Monto: ')
        indice_cliente=input('Clave: ')

        return numero, destino, monto, indice_cliente

    def mostrar_fletes(self, diccionario):
        if not diccionario:
            print("No hay fletes")
        else:
            for items in diccionario.values():
                print(items)

    def mostrar_cliente(self, diccionario):
        if not diccionario:
            print("No hay clientes almacenados")
        else:
            """
            Dado que el codigo del cliente se guarda como llave, se extraen los valores. 
            Esto difiere de la firma de extraer los fletes
            """
            for clave, valor in diccionario.items():
                print(clave, '-', valor)

    def mostrar_Messaje(self, mensaje):
        print(mensaje)