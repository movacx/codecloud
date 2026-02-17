class HuespedModel:
	def __init__(self, ide, nombre, telefono):
		self.ide = ide
		self.nombre = nombre
		self.telefono = telefono
		
	def getId(self):
		return self.ide
	def setId(self, ide):
		self.ide = ide
	
	def getNombre(self):
		return self.nombre
	
	def importarToCsv(self):
		return ([self.ide,self.nombre,self.telefono])
	