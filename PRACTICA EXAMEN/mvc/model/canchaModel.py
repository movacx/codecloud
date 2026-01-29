class CanchaModel:
    def __init__(self, numero,tipo,tarifa_hora,estado):
        self.numero = numero
        self.tarifa = tarifa_hora
        self.estado = estado
    
    def importTocsv(self):
        return ([self.numero,self.tipo,self.tarifa_hora,self.estado])
    