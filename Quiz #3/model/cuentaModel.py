class Cuenta:
    
    def __init__(self,numeroCuenta, dniCliente, saldo=0):
        self.numeroCuenta=numeroCuenta
        self.dniCliente=dniCliente
        self.saldo=saldo
        
    def depositar(self, monto):
        if monto>0:
            self.saldo+= monto
            print(f"Deposito exitoso saldo actualizado: {self.saldo}")
        else:
            print("El monto a despositar es positivo")
            
    def retirar(self, monto):
        if 0<monto <= self.saldo:
            self.saldo-= monto
            print(f"Retiro exitoso saldo actualizado: {self.saldo}")
        else:
            print("Fondos insuficientes ")
            
            
    def importarCsv(self):
        return [(self.numeroCuenta, self.dniCliente, self.saldo)]
        
    
        
    
        
        
    