from Model.empleadoModel import Empleado

class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, idEmpleado, horasTrabajadas, tarifaPorHora):
        super().__init__(nombre, idEmpleado)
        self.horasTrabajadas = horasTrabajadas
        self.tarifaPorHora = tarifaPorHora

    # SOBRESCRIBIMOS EL MÉTODO (Polimorfismo)
    def calcularSalario(self):
        # Aquí hay matemática distinta
        calculo = self.horasTrabajadas * self.tarifaPorHora
        return calculo

    def mostrarDatos(self):
        return f"{super().mostrarDatos()} | Tipo: Por Hora | Pago: ${self.calcularSalario()}"