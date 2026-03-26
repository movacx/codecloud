class Cliente:
    def __init__(self, cedula, nombre, carrera):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = carrera
    
    def __str__(self):
        return f"""
Numero de cedula: {self.cedula}
Nombre del estudiante: {self.nombre}
Carrera: {self.carrera}"""
    
