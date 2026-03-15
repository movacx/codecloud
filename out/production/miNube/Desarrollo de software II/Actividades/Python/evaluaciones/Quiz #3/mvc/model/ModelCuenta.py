class Cuenta:
    def __init__(self, numero_cuenta, dni_cliente, saldo):
        self.numero_cuenta = numero_cuenta
        self.dni_cliente = dni_cliente
        self.saldo = saldo
        
    def depositar(self, monto):
        self.saldo += monto
    
    def retirar(self, monto):
        self.saldo -= monto
    
        
    def exportar(self):
        return ([self.dni_cliente,self.numero_cuenta, self.saldo])