from Model.cuentaModel import CuentaModel

class CuentaAhorro(CuentaModel):
	def __init__(self, numeroCuenta, dniCliente, saldo, interesAnual):
		super().__init__(numeroCuenta,dniCliente,saldo)
		self.interesAnual = interesAnual
#-------------------------------------------------Metodos---------------------------------------------------------

	def aplicarIntereses(self):
		if self.interesAnual  > 0:
			interesCalculado = self.saldo * self.interesAnual
			self.saldo = self.saldo + interesCalculado
			return True
		return False
	
	
	def importToCsv(self):
		return (["AHORRO: ", self.numeroCuenta, self.dniCliente, self.saldo, self.interesAnual])
		
	