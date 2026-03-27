'''Modulo del controlador del sistema de pagos
Responsabilidad:
    -Recibir la opcion seleccionada
    -Determinar que metodo de pago usar
    -validar el monto
    -Ejecutar el pago

Relacion con SOLID
1. SRP
    -El controlador coordina el flujo del pago.
    -No imprime menus ni implementa directamente
2. OCP
    -El diseño del sistema permite agregar nuevas clases de pago
    -En esta versin simple del MVC, si se agrega una opcion en el Menu
3. LSP
    -El controlador trabaja con objetos que cumlen con el contrato MetodoPago
4. DIP
    -El controlador depende la abstraccion MetodoPago a traves del uso de las clases del modelo, no de la implementacion interna de cada pago
'''

from Model.metodo_pago import MetodoPago
from Model.metodo_pago import PagoEfectivo
from Model.metodo_pago import PagoTarjeta
from Model.metodo_pago import PagoTransferencia


class Procesador_pago:
    '''Controlador principal del flujo de pagos'''
    def crear_metodo_pago(self, opcion:str) -> MetodoPago:
        '''
        Crea u retorna el metodo de pago correspondiente segun la opcion elegida por el usuario.
        Opcion: opcion elegida por el usuario
        return: instancia de una clase que hereda de metodoPago
        raise ValueError: La opcion es invalida

        SOLID:
        -LSP: Retorna cualquier subtipo de MetodoPago
        -DIP: El metodo devuelve la abstraccion MetodoPago
        '''

        if opcion == '1':
            return PagoTarjeta()
        elif opcion == '2':
            return PagoEfectivo()
        elif opcion == '3':
            return PagoTransferencia
        raise ValueError('Opcion invalida. Debe seleccionar una opcion del 1 al 4')