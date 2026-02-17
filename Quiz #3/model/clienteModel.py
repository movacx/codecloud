class Cliente:
    
    def __init__(self, dni, nombre, apellido, email):
        self.dni=dni
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
            
    def getDni(self):
        return self.dni
    
    def setDni(self,dni):
        self.dni=dni
        
        
    def importarCsv(self):
        return [(self.dni, self.nombre, self.apellido, self.email)]
        
        
        
        