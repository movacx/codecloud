class GastosModel:
    
    def __init__(self, ide, descripcion, monto, categoria, fecha):
        self.id = ide
        self.descripcion = descripcion
        self.monto = monto
        self.categoria = categoria
        self.fecha = fecha
        
    def getId(self):
        return self.ide
    
    def setId(self, nuevoId):
        self.ide = nuevoId
    
    def importTocsv(self):
        return ([self.id, self.descripcion, self.monto,self.categoria,self.fecha])