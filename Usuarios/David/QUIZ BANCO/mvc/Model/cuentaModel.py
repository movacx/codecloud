class CuentaModel:
	def __init__(self,numeroCuenta, dniCliente, saldo):
		self.numeroCuenta = numeroCuenta
		self.dniCliente = dniCliente
		self.saldo = saldo
#-------------------------------------------------Metodos--------------------------------------------------------------
def depositarMonto(self, monto):
	if monto > 0:
		self.saldo += monto
		return True
	return False 


def retirarMonto(self, monto):
	if monto > 0 and monto <= self.saldo:
		self.saldo = self.saldo - monto
		return True
	return False


def importToCsv(self):
	return ([self.numeroCuenta, self.dniCliente, self.saldo])