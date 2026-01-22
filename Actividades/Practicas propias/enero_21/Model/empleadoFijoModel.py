from Model.empleadoModel import Empleado

class EmpleadoFijo(Empleado):
    def __init__(self, nombre, idEmpleado, salarioBase):
        super().__init__(nombre, idEmpleado)
        self.salarioBase = salarioBase

    # SOBRESCRIBIMOS EL MÉTODO (Polimorfismo)
    def calcularSalario(self):
        return self.salarioBase 

    def mostrarDatos(self):
        return f"{super().mostrarDatos()} | Tipo: Fijo | Pago: ${self.calcularSalario()}"