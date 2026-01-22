class Empleado:
    def __init__(self, nombre, idEmpleado):
        self.nombre = nombre
        self.idEmpleado = idEmpleado

    #Getters
    def getNombre(self):
        return self.nombre
    def getId(self):
        return self.idEmpleado
    
    #----- Polimorfismo --- #
    #Este metodo sera sobreEscrito por los hijos
    def calcularSalario(self):
        return 0
    
    def mostrarDatos(self):
        return f"Id: {self.idEmpleado} | Nombre: {self.nombre}"