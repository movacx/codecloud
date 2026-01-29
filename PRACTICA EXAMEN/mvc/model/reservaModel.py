class Reserva:
	def __init__(self,id, numeroCancha, idSocio, fecha, horaInicio, horaFin):
		self. numeroCancha = numenumeroCancha
		self.idSocio = idSocio
		self.fecha = fecha
		self.horaInicio = horaInicio
		self.horaFin = horaFin
#---------------------------------------------------------------------------------------------#		
	#Get y set ID
	def getId(self):
		return self.id
	
	def setId(self, id):
		self.id = id
#---------------------------------------------------------------------------------------------#			
#Metodo importToCsv
	def importToCsv(self):
		return ([self.numeroCancha, self.idSocio, self.fecha, self.horaInicio, self.horaFin])
	
	
		