'''Modulo de la vista del sistema
Responsabilidad:
-Mostrar informacion por la consola
-Solicitar datos al usuario
-Presemtar resultados y errores

Relacion con SOLID
    SRP: La vista se encarga de interaccion con el usuario
    No contiene logica de negocio ni logica de validacion
'''

class VistaConsola:
    '''
    Clase de interfaz por consola
    '''
    @staticmethod
    def mostrar_menu()-> str:
        '''Muestra el menu principal del sistema'''

        return input('''
===============Sistema de pagos====================
1. pago con tarjeta
2. pago en efectivo
3. pago por transferencia
0. salir
Input: ''')
    
