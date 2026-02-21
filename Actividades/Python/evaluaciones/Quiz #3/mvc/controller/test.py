from view.CreditosView import CreditosGUI

class ControllerCreditos:
    def __init__(self, root,):
        self.GUI = CreditosGUI(root, self)
        self.modo = ''
        
    def solicitarEstado(self):
        self.modo = 'solicitar'
        
    def recibirAccion(self):
        if self.modo == 'solicitar':
            print('hola mundo')


