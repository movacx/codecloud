from Controller.nominaController import NominaController
import View.empleadoView as vista

controlador = NominaController()
opcion = 0
def main():
    while True:
        vista.menuPrincipal()
        try:
            opcion = int(input("Ingrese una opcion: "))

            if opcion == 1:
                vista.mostrarMensaje("----Empleado Fijo----")
                nombre = input("Nombre: ")
                cedula = input("Cedula: ")
                salario = input("Salario Mensual: ")
                controlador.agregarFijo(nombre,cedula,salario)
                continue
            elif opcion == 2:
                vista.mostrarMensaje("----Empleado Por Hora----")
                nom = input("Nombre: ")
                cedula = input("ID: ")
                horas = int(input("Horas Trabajadas: "))
                tarifa = float(input("Tarifa por Hora: "))
                controlador.agregarPorHora(nom, cedula, horas, tarifa)
                continue
            elif opcion == 3:
                controlador.mostrarNomina()
                continue
            elif opcion == 4:
                cedula = input("Cedula: ")
                controlador.eliminarEmpleados(cedula) 
                continue
            elif opcion == 5:
                vista.mostrarMensaje("Saliendo del sistema............")
                break
            else:
                vista.mostrarMensaje("Opcion invalida")

        except ValueError:
            vista.mostrarMensaje("Ingrese numeros validos")
            print("HelloWOrld")

if __name__ == "__main__":
    main()