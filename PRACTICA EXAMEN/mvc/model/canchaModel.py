class CanchaModel:
    def __init__(self, numero,tipo,tarifa_hora,estado):
        self.numero = numero
        self.tipo = tipo
        self.tarifa_hora = tarifa_hora
        self.estado = estado
    
    def setEstado(self, nuevoEstado):
        self.estado = nuevoEstado
        
    def getEstado(self):
        return self.estado
    
    def importTocsv(self):
        return ([self.numero, self.tipo, self.tarifa_hora, self.estado])
    