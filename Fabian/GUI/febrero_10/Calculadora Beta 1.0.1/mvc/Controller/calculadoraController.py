# from Data.calculadoraData import Data
from Model.calculadoraModel import Model
from View.calculadoraGUI import calculadora
from Data.calculadoraData import Data

class Controller:
    
    def __init__(self, root):
        self.texto_actual = ''
        self.num_guardado = 0 #Se guarda el primer numero
        self.operador = '' #Se guarda el signo de la operacion

        self.modelo = Model()
        self.GUI = calculadora(root, self)
        self.manejoData = Data()


    def recibirNumero(self, boton):
        if boton == '1':
            self.texto_actual += '1'
        elif boton == '2':
            self.texto_actual += '2'
        elif boton == '3':
            self.texto_actual += '3'
        elif boton == '4':
            self.texto_actual += '4'
        elif boton == '5':
            self.texto_actual += '5'
        elif boton == '6':
            self.texto_actual += '6'
        elif boton == '7':
            self.texto_actual += '7'
        elif boton == '8':
            self.texto_actual += '8'
        elif boton == '9':
            self.texto_actual += '9'
        elif boton == '0':
            self.texto_actual += '0'
        elif boton == '.':
            if '.' not in self.texto_actual: 
                self.texto_actual += '.'        

        self.GUI.actualizar_pantalla(self.texto_actual)
        


    def recibirMatch(self, matchButton):
        if matchButton == '+':
            self.num_guardado = float(self.texto_actual)
            self.operador = '+'
            self.texto_actual = ''
            self.GUI.actualizar_pantalla('')

            return
        elif matchButton == '-':
            self.num_guardado = float(self.texto_actual)
            self.operador = '-'
            self.texto_actual = ''
            self.GUI.actualizar_pantalla('')
            return 
        elif matchButton == '/':
            self.num_guardado = float(self.texto_actual)
            self.operador = '/'
            self.texto_actual = ''
            self.GUI.actualizar_pantalla('')
            return 
        elif matchButton == '*':
            self.num_guardado = float(self.texto_actual)
            self.operador = '*'
            self.texto_actual = ''
            self.GUI.actualizar_pantalla('')
            return 
        elif matchButton == '=':
            segundo_numero = float(self.texto_actual)

            if self.operador == '+':
                resultado = self.modelo.sumar(self.num_guardado, segundo_numero)
            elif self.operador == '-':
                resultado = self.modelo.restar(self.num_guardado, segundo_numero)
            elif self.operador == '*':
                resultado = self.modelo.multiplicar(self.num_guardado, segundo_numero)
            elif self.operador == '/':
                resultado = self.modelo.dividir(self.num_guardado, segundo_numero)
            
            self.texto_actual = str(resultado)

            self.GUI.actualizar_pantalla(self.texto_actual)
            
            self.manejoData.registrarHistorial(self.modelo)

            imprimir = f'{self.num_guardado} + {segundo_numero} = {resultado}'

            self.GUI.mostrar_historial(imprimir)

        elif matchButton == 'C':
            self.texto_actual = ''
            self.num_guardado = 0
            self.operador = ''
            self.GUI.actualizar_pantalla('')