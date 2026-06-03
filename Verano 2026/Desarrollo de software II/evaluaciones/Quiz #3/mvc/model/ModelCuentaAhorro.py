from ModelCuenta import Cuenta
class CuentaAhorro(Cuenta):
    def __init__(self, numero_cuenta, dni_cliente, saldo, interes_anual):
        super().__init__(numero_cuenta, dni_cliente, saldo)
        self.interes_anual = interes_anual
        
    
    def aplicar_interes(self):
        self.saldo += self.saldo * self.interes_anual
    
    def exportar(self):
        return ([self.numero_cuenta, self.dni_cliente, self.saldo, self.interes_anual])