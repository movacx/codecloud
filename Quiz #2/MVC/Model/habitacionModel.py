class HabitacionModel:
	
	def __init__(self,id, numero, tipo, precio, estado):
		self.id = id
		self.numero = numero
		self.tipo = tipo
		self.precio = precio
		self.estado = estado
	
def getId(self):
	return self.id

def setId(self, id):
	self.id = id


def importarToCsv(self):
	return ([self.id, self.numero, self.tipo, self.precio, self.estado])

def mostrarDatos():
	return f"Numero : {self.numero}, Tipo: {self.tipo}, Precio: {self.precio}, Estado: {self.estado}" 
