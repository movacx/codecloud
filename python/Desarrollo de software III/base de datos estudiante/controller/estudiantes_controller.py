from service.estudiante_service import EstudianteService

class EstudianteController:
    def __init__(self):
        self.service = EstudianteService

    def mostrar_menu(self):
        opcion=''

        while opcion != '6':
            print('\n-=-=-==--=-=-=-=-=-=-==--==--=-=-=-=')
            print('\nSISTEMA GESTOR DE ESTUDIANTES')
            print('-=-=-==--=-=-=-=-=-=-==--==--=-=-=-=')
            print('1. Registrar estudiante')
            print('2. Consultar estudiante')
            print('3. Buscar estudiante')
            print('4. Actualizar estudiante')
            print('5. Eliminar estudiante')
            print('6. Salir')

            opcion = input('Seleccione una opcion')
            if opcion == '1':
                self.registrar()
            elif opcion == '2':
                self.consultar()
            elif opcion == '3':
                self.buscar()
            elif opcion == '4':
                self.actualizar()
            elif opcion == '5':
                self.eliminar()
            elif opcion == '6':
                print('Saliendo del sistema')
                break
            else:
                print('opcion invalida')
