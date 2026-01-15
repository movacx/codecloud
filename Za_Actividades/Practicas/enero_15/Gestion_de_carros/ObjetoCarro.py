class Carro:
    idVehiculo = 0
    def __init__(self, marca,modelo,color,placa ):
        Carro.idVehiculo += 1
        self.id = Carro.idVehiculo
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    #Seccion de getters
    def getPlaca(self):
        return self.placa
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getColor(self):
        return self.color
    def getId(self):
        return self.id
    
    #Seccion de setters
    def setPlaca(self, nuevaPlaca):
        self.placa = nuevaPlaca
    def setMarca(self, nuevaMarca):
        self.marca = nuevaMarca
    def setModelo(self, nuevoModelo):
        self.modelo = nuevoModelo
    def setColor(self, nuevoColor):
        self.color = nuevoColor
    
    def __str__(self):
        return f"""Sistema de Gestión de Carros
    Marca: {self.marca}
    Modelo: {self.modelo}
    Color: {self.color}
    Identificador: {self.id}"""
        
    def mostrarRegistros(self):
        return f"Identificador: {self.id}", self.placa, self.marca, self.modelo, self.color
    
    
        