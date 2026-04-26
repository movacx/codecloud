class Model:
    def __init__(self):
        self.numUno = 0
        self.numDos = 0
        self.resultado = 0
        self.operacion = ''
        self.fechaHora = ''

    def setFecha(self, nuevaHora):
        self.fechaHora = nuevaHora

    def setOperacion(self, nuevoDato):
        self.operacion = nuevoDato

    def setFechaHora(self, fecha):
        self.fechaHora = fecha

    def restar(self, num1, num2):
        self.numUno = num1 
        self.numDos = num2
        self.resultado = num1 - num2
        return self.resultado

    def sumar(self, num1, num2):
        self.numUno = num1
        self.numDos = num2
        self.resultado = num1 + num2
        return self.resultado

    def multiplicar(self, num1, num2):
        self.numUno = num1
        self.numDos = num2
        self.resultado = num1 * num2
        return self.resultado

    def dividir(self, num1, num2):
        self.numUno = num1
        self.numDos = num2
        self.resultado = num1 / num2
        return self.resultado
    
    

    def importar(self):
        return [self.numUno, self.operacion, self.numDos, self.resultado, self.fechaHora]