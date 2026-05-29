'''
Esta clase contiene las reglas de negocio y validaciones
El service usa al repositorio para guardar, consultar,
actualizar o eliminar, pero antes valida que los datos sean correctos
'''

from repository.estudiante_repository import EstudianteRepository
from model.estudiante import Estudiante


class EstudianteService:
    '''
    Servicio que contiene la logica del negocio de estudiantes
    '''

    def __init__(self):

        # Se crea una instancia del repositorio
        self.repository = EstudianteRepository()

    def registrar_estudiantes(self, nombre, correo, carrera):
        '''
        Valida y registra un estudiante
        '''

        nombre = nombre.strip()
        correo = correo.strip()
        carrera = carrera.strip()

        # Validacion campos vacios

        if nombre == '' or correo == '' or carrera == '':
            return 'Error: Todos los campos son obligatorios'

        # Validacion correo

        if '@' not in correo or '.' not in correo:
            return 'Error: Formato del correo invalido'

        # Validar correo repetido

        if self.repository.existe_correo(correo):
            return 'Error: Ya existe un estudiante con ese correo'

        nuevo = Estudiante(
            nombre=nombre,
            correo=correo,
            carrera=carrera
        )

        self.repository.registrar(nuevo)

        return 'Estudiante registrado correctamente'

    def consultar_estudiante(self):

        return self.repository.consultar_todos()

    def busacr_estudiante(self, id_estudiante):

        return self.repository.busacar_por_id(id_estudiante)

    def actualizar_estudiante(self, id_estudiante, nombre, correo, carrera):
        '''
        Actualiza un estudiante
        '''

        nombre = nombre.strip()
        correo = correo.strip()
        carrera = carrera.strip()

        # Verificar existencia

        estudiante_existente = self.repository.busacar_por_id(id_estudiante)

        if estudiante_existente is None:
            return 'Error: No existe un estudiante con ese ID'

        # Crear objeto actualizado

        nuevo = Estudiante(
            id_estudiante=id_estudiante,
            nombre=nombre,
            correo=correo,
            carrera=carrera
        )

        actualizado = self.repository.actualizar(nuevo)

        if actualizado:
            return 'Estudiante actualizado correctamente'

        return 'Error: No se pudo actualizar el estudiante'

    def eliminar_estudiante(self, id_estudiante):

        estudiante_eliminado = self.repository.eliminar(id_estudiante)

        if estudiante_eliminado:
            return 'Estudiante eliminado correctamente'

        return 'Error: No se pudo eliminar el estudiante'