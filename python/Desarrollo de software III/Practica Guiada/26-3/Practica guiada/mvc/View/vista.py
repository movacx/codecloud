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
    
    @staticmethod
    def solicitar_monto() -> float:
        return float(input('Ingresar el monto a ingresar: '))
    
    @staticmethod
    def mostrar_resultado(mensaje:str) -> None:
        print(f'\n Resultado: {mensaje}')

    @staticmethod
    def mostrar_error(error:str) -> None:
        print(f'\n Error: {error}')
