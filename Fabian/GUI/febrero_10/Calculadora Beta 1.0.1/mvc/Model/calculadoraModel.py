class Model:

    def __init__(self):
        self.resultado = 0
        self.num_uno = 0
        self.num_dos = 0

    def restar(self, num1, num2):
        self.num_uno = num1 
        self.num_dos = num2
        self.resultado = num1 - num2
        return self.resultado

    def sumar(self, num1, num2):
        self.num_uno = num1
        self.num_dos = num2
        self.resultado = num1 + num2
        return self.resultado

    def multiplicar(self, num1, num2):
        self.num_uno = num1
        self.num_dos = num2
        self.resultado = num1 * num2
        return self.resultado

    def dividir(self, num1, num2):
        self.num_uno = num1
        self.num_dos = num2
        if num2 != 0:
            self.resultado = num1 / num2
        else:
            self.resultado = "Error"
        return self.resultado

    def importar(self):
        return ([self.num_uno, self.num_dos, self.resultado])