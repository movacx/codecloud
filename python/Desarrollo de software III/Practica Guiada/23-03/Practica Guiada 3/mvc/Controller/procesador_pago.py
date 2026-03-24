'''
Controlador con diseño deficiente

Problemas:
    Es estupido.
    El controlador depende completamente de una clase concreta: Sistema_pagos
    No usa abstracciones
    El controlador aporta poco valor arquitectonico porque casi toda la logica esta dentro del modelo

Violacion:
    -DIP: Depende directamente de Sistemas_pagos, una implementacion concreta.
'''

from Model.metodo_pago import Sistemas_pagos

class ControladorPagos:
    'Controlador que delega casi tod0 en una clase del modelo'
    def __init__(self):
        '''
        Violacion de DIP:
            Se instancia directamente una clase concreta
        '''
        self.sistema = Sistemas_pagos()

    def iniciar(self):
        '''
        Ejecuta el sistema en bucle, aunque aqui hay un ciclo funcional, el diseño general sigue siendo malo
        pues tod0 se apoya en una clase demasiada acoplada.
        '''
        while True:
            try:

                opcion = self.sistema.mostrar_menu()
                if opcion == 4:
                    print('\n Saliendo del sistema')
                    self.sistema.mostrar_historial()
                    break
                monto = self.sistema.solicitar_monto()
                resultado = self.sistema.procesar_pago(opcion, monto)
                print('Resultado', resultado)

            except ValueError as error:
                print(f'Error {error}')
            except Exception as error2:
                print(f'Ha ocurrido un error mi rey {error2}')
