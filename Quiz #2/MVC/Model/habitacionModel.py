class HabitacionModel:
	
	def __init__(self,ide, numero, tipo, precio, estado):
		self.ide = ide
		self.numero = numero
		self.tipo = tipo
		self.precio = precio
		self.estado = estado
	
	def getId(self):
		return self.ide
	def setId(self, ide):
		self.ide = ide
        
	def importarToCsv(self):
		return ([self.ide, self.numero, self.tipo, self.precio, self.estado])
