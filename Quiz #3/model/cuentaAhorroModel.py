class CuentaAhorro(Cuenta):
    
    def __init__(self, numeroCuenta, dniCliente, saldo, interesAnual):
       super().__init__(numeroCuenta, diniCliente, saldo)
       self.interesAnual=interesAnual
       
       def aplicarInteres(self):
           interesGanado=self.saldo * self.interesAnual
           self.saldo+=interesGanado
           print(f"Interes aplicado: {interesGanado} saldo total: {self.saldo}")
           
           
        def importarCsv(self):
            return [(self.numeroCuenta, self.dniCliente, self.saldo, self.interesAnual)]
