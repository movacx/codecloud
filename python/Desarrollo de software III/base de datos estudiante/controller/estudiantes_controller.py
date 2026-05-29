from service.estudiante_service import EstudianteService


class EstudianteController:

    def __init__(self):
        self.service = EstudianteService()

    def mostrar_menu(self):

        opcion = ''

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

            opcion = input('Seleccione una opcion: ')

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
                print('Opcion invalida')

    def registrar(self):
        '''
        Solicita los datos de un estudiante
        '''

        print('\n --------- Registrar Estudiante --------------')

        nombre = input('Nombre completo: ')
        correo = input('Correo electronico: ')
        carrera = input('Carrera: ')

        mensaje = self.service.registrar_estudiantes(
            nombre,
            correo,
            carrera
        )

        print(mensaje)

    def consultar(self):
        '''
        Consulta todos los estudiantes
        '''

        print('\n ------- Lista de estudiantes ------ ')

        estudiantes = self.service.consultar_estudiante()

        if len(estudiantes) == 0:
            print('No hay estudiantes registrados')
            return

        for estudiante in estudiantes:
            print(estudiante)

    def buscar(self):
        '''
        Busca un estudiante por ID
        '''

        print('\n--- Buscar estudiante ----')

        try:
            id_estudiante = int(input('Digite el id del estudiante: '))

        except ValueError:
            print('Error: el id debe ser un numero')
            return

        estudiante = self.service.busacr_estudiante(id_estudiante)

        if estudiante is None:
            print('No se encontro ningun estudiante con ese ID')

        else:
            print(estudiante)

    def actualizar(self):
        '''
        Actualiza un estudiante
        '''

        print('\n ------- Actualizar estudiante ---- ')

        try:
            id_estudiante = int(input('Digite el id del estudiante: '))

        except ValueError:
            print('Error: el id debe ser un numero')
            return

        estudiante = self.service.busacr_estudiante(id_estudiante)

        if estudiante is None:
            print('No existe un estudiante con ese ID')
            return

        print('Datos actuales')
        print(estudiante)

        print('Digite los nuevos datos')

        nombre = input('Nombre completo: ')
        correo = input('Correo electronico: ')
        carrera = input('Carrera: ')

        mensaje = self.service.actualizar_estudiante(
            id_estudiante,
            nombre,
            correo,
            carrera
        )

        print(mensaje)

    def eliminar(self):
        '''
        Elimina un estudiante
        '''

        print('\n ------- Eliminar estudiante ---- ')

        try:
            id_estudiante = int(input('Digite el id del estudiante: '))

        except ValueError:
            print('Error: el id debe ser un numero')
            return

        estudiante = self.service.busacr_estudiante(id_estudiante)

        if estudiante is None:
            print('No se encontro ningun estudiante con ese ID')
            return

        print('Estudiante encontrado')
        print(estudiante)

        confirmacion = input('Esta seguro de eliminarlo? (si/no): ')

        if confirmacion.lower() == 'si':

            mensaje = self.service.eliminar_estudiante(id_estudiante)

            print(mensaje)

        else:
            print('Operacion cancelada')