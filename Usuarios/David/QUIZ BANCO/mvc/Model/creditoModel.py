class CreditoModel():
	def __init__(self, idCredito, dniCliente, montoPrestado, cuotasTotales, cuotasPagadas, estado):
		self.idCredito = idCredito
		self.dniCliente = dniCliente
		self.montoPrestado = montoPrestado
		self.cuotasTotales = cuotasTotales
		self.cuotasPagadas = cuotasPagadas
		self.estado = estado
		
		
	#SET Y GET
	def setIdCredito(self, idCredito):
		self.idCredito = idCredito

	def getIdCredito(self):
		return self.idCredito
	
#-------------------------------------------------Metodos---------------------------------------------------------
	def pagarCuota(self,monto):
		if self.estado != "Activo":
			return False
		
		if monto <=0:
			return False
		
		if self.cuotasPagadas < self.cuotasTotales:
			self.cuotasPagadas = self.cuotasPagadas + 1
			
			if self.cuotasPagadas >= self.cuotasTotales:
				self.estado = "Finalizado"
				
			return True
		
		self.estado = "Finalizado"
		return False
	
	def importToCsv(self):
		return ([self.idCredito, self.dniCliente, self.montoPrestado, self.cuotasTotales, self.cuotasPagadas, self.estado])
	
	

