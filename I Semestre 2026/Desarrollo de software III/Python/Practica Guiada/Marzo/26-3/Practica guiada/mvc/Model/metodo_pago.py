'''Modulo del modelo relacionado con los metodos de pago
aquise define:
-Una abstraccion general para los metodos de pago
-implementacion concretas de cada tipo de pago


Relacon con SOLID:
1. SRP (Responsabilidad unica)
-cada clase concreta tiene una unica responsabilidad:
    ejecutar un tipo especifico de pago

2. OCP(Abierto y cerrado)
El sistema esta abierto a extension:
Se pueden agregar nuevos metodos de pago creando nuevas clases
sin modifcar las existentes

3. LSP(Sustitucion de liskov)
Cualquier clase hija puede sustituir a metodo_oagi sin romper el
comportamiento esperado del sistema.

4. ISP(Segregacion de interfaz)
    La abstraccion Metodo_pago define una interfaz pequeña y especifica:
    Solo exige implementar el metodo pagar

5. DIP(Inversion de dependencia)
    El resto del sistema depende de la abstraccion metodo pago,
    no directamente de pago_tarjeta, pago_efectivo, etc

'''

from abc import ABC, abstractmethod

class MetodoPago(ABC):
    def __init__(self):
        '''Clase abstracta que representa el contrao general de cualquier metodo de pago

        SOLID:
        ISP: interfaz pequeña y espeifica
        DIP el sistema depende de esta abstraccion
        '''

        @abstractmethod
        def pagar(self, monto: float):
            '''
            Procesa un pago y retorna un mensaje descriptivo
            monto: Monto a pagar
            mensaje del resultado de paga
            '''
            pass

class PagoTarjeta(MetodoPago):
    '''
    Implementacion concreta del pago con tarjeta
    
    SOLID:
    -SRP: Esta clase solo gestiona el pago con tarjeta
    -LSP: Puede usarse donde se espere un MetodoPago
    '''
    def pagar(self, monto:float) -> str:
        return f'Pagando{monto:.2f} con tarjeta'
    
class PagoEfectivo(MetodoPago):
    '''
    Implementacion concreta del pago con tarjeta
    
    SOLID:
    -SRP: Esta clase solo gestiona el pago con tarjeta
    -LSP: Puede usarse donde se espere un MetodoPago
    '''
    def pagar(self, monto:float) -> str:
        return f'Pagando{monto:.2f} en efectivo'
    
class PagoTransferencia(MetodoPago):
    '''
    Implementacion concreta del pago con tarjeta
    
    SOLID:
    -SRP: Esta clase solo gestiona el pago con tarjeta
    -LSP: Puede usarse donde se espere un MetodoPago
    '''
    def pagar(self, monto:float) -> str:
        return f'Pagando{monto:.2f} por transferencia'