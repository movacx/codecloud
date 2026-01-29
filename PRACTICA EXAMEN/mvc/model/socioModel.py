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
		self.id = iid
#---------------------------------------------------------------------------------------------#		
	#ImportToCsv
	def importToCsv():
		return  ([self.nombre, self.telefono])