class ClienteModel:
	def __init__(self, dni, nombre, apellido, email):
		self.dni = dni
		self.nombre = nombre
		self.apellido = apellido
		self.email = email
#------------------------------------------------------------------------------------------------------------------------
	def importToCsv(self):
		return ([self.dni, self.nombre, self.apellido, self.email])
		
	