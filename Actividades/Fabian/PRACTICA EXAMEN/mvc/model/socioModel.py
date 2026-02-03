class Socio:
	def __init__(self, id, nombre, telefono):
		self.id = id
		self.nombre = nombre
		self.telefono = telefono
#---------------------------------------------------------------------------------------------#		
	#Get y set del ID
	def getId(self):
		return self.id
	
	def setId(self, id):
		self.id = id
#---------------------------------------------------------------------------------------------#		
	#ImportToCsv
	def importToCsv(self):
		return  ([self.id, self.nombre, self.telefono])