'''
clase con mal diseño intencionalmente, este archivo viola multiples principios solid:

1. SRP(Responsabilidad única )
    La clase tiene muchas responsabilidades, entre ellas:
        ° Muestra mensajes
        ° Valida datos
        ° Procesa pagos
        ° Decide que tipo de pagos usar
        ° Genera historial

2. OCP(Cerrado a modificaciones, abierto a extensión)
    Cada vez que se agrega un nuevo metodo de pago, hay que modificar el metodo procesar_pago()

3. ISP (Segregación de interfaces)
    No existen interfaces pequeñas ni especializadas

3. DIP(Inversion de dependencias)
    La clase depende directamente de detalles concretos no de abstracciones
        Tambien viola:
            *DRY: Repite lógica y mensajes
            *KISS (Rita): La clase hace demasiado
            *Demeter: Mezcla responsabilidades y accede a demasiados detalles

'''

class Sistemas_pagos:
    '''
    Clase monolitica que centraliza toda la logica del sistema
    Este es un ejemplo de como no se debe de diseñar el sistema
    '''
    def __init__(self): #'Guarda el historial y estado interno'

        self.historial = []

    def mostrar_menu(self):
        'Violacion de SRP. Esta clase en el modelo no debe mostrar interfaz'
        'Desde el modelo no deben pedir datos. Violacion DE SRP'
        try:
            return int(input('''
            ===Sistema de pagos===
            1. Pago con tarjeta
            2. Pago en efectivo
            3. pago por transferencia
            0. Salir
            input: '''))
        except ValueError:
            print('Debe de ingresar numeros pedazo de imbecil')


    def solicitar_monto(self):
        return float(input('Ingrese un monto a pagar: '))

    def validar_monto(self, monto):
        'Violacion de SRP La validacion debe estar separada'
        if monto <=0:
            raise ValueError('El monto debe ser mayor a cero')

    def procesar_pago(self, opcion, monto):
        '''
        Metodo altamente acoplado y poco extensible
            Violaciones:
                *OCP: Para agregar un nuevo metodo de pago hay que modificar este metodo.
                *DIP: Depende directamente de condicionales concretas
                *DRY: Repite estructura logica
        '''
        self.validar_monto(monto)

        if opcion == 1:
            mensaje = f'Pagando {monto: .2f} con tarjeta'
            print(mensaje)
            self.historial.append(mensaje)
            return mensaje
        elif opcion == 2:
            mensaje = f'Pagando {monto: .2f} con efectivo'
            print(mensaje)
            self.historial.append(mensaje)
            return mensaje

        elif opcion == 3:
            mensaje = f'Pagando {monto: .2f} por transferencia'
            print(mensaje)
            self.historial.append(mensaje)
            return mensaje

        elif opcion == 0:
            return 'Saliendo del sistema'
        else:
            raise ValueError('Opcion invalida')



    def mostrar_historial(self):
        '''
        Violacion de SRP:
            Ademas de procesar pagos la clase tambien administra y muestra el historial
        '''

        print('\n===========Historial de pagos===========')
        if len(self.historial) == 0:
            print('no hay datos')
        else:
            for pago in self.historial:
                print(pago)




