class Reportes:
	
	idReportes = 0
	def __init__(self, listadoProductos, reportesProductos, historialMovimientos):
		self.listadoProductos = listadoProductos
		self.reportesProductos = reportesProductos
		self. historialMovimientos = historialMovimientos
		Reportes.idReportes += 1
		self.id = Reportes.idReportes
		
		
	#Getters
	