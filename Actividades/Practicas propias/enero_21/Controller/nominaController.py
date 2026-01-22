from Model.empleadoFijoModel import EmpleadoFijo
from Model.empleadoHoraModel import EmpleadoPorHora
import View.empleadoView as vista

class NominaController:
    def __init__(self):
        self.listaEmpleados = []
    
    #Agregar
    def agregarFijo(self, nombre, idEmpleado, salario):
        nuevoFijo = EmpleadoFijo(nombre, idEmpleado, salario)
        self.listaEmpleados.append(nuevoFijo)
        vista.mostrarMensaje("Empleado Fijo Agregado")

    #AgregarPorHora
    def agregarPorHora(self, nombre, idEmpleado, horas, tarifaPorHora):
        nuevoHora = EmpleadoPorHora(nombre, idEmpleado, horas, tarifaPorHora)
        self.listaEmpleados.append(nuevoHora)
    
    #Mostrar (Polimorfismo)
    def mostrarNomina(self):
        if not self.listaEmpleados:
            vista.mostrarMensaje("No hay empleados registrados")
        else:
            vista.mostrarMensaje("---Lista de Empleados----")
            for items in self.listaEmpleados:
                vista.mostrarTodos(items.mostrarDatos())

    def eliminarEmpleados(self, idBuscar):
        for items in self.listaEmpleados:
            if items.getId() == idBuscar:
                self.listaEmpleados.remove(items)
                return vista.mostrarMensaje("Empleado eliminado")
        return vista.mostrarMensaje("No encontrado")
    
