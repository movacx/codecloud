class Gastos:
	def __init__(self, id, descripcion, monto, categoria, fecha):
		self.ide = id
		self.descripcion = descripcion
		self.monto = monto
		self.categoria = categoria
		self.fecha = fecha

	def getId(self):
		return self.id
	
	def setId(self, id):
		self.id = id
	
	def importToCsv(self):
		return ([self.id,self.descripcion,self.monto,self.categoria,self.fecha])

