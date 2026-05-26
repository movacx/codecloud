'''
Esta clase contiene las reglas de negocio y validaciones
El service usa al repositorio para guardar, consultar, actualizar o eliminar, pero antes valida que los datos sean
correctos
'''
from repository.estudiante_repository import EstudianteRepository
from model.estudiante import Estudiante
class EstudianteService:
    '''
    Servicio que contiene la logica del negocio de estudiantes
    '''
    def __init__(self):
        #Se crea una instancia del repositorio para acceder a la base de datos
        self.repository=EstudianteRepository()

    def registrar_estudiantes(self, nombre, correo,carrera):
        '''Valida y registra un estudiante
        nombre completo del estudiante, correo y carrera'''

        #strip elimina los espacios en blanco al inicio y al final
        nombre = nombre.strip()
        correo = correo.strip()
        carrera = carrera.strip()#club

        #Validacion: ningun campo debe estar vacio

        if nombre == '' or correo =='' or carrera == '':
            return 'Error: Todos los campos son obligatorios'
        
        #Validacion basica del correo
        if '@' not in correo or '.' not in correo:
            return 'Error: Formato del correo invalido'
        
        #Validacion: el correo no debe repetirse

        if self.repository.existe_correo(correo):
            return 'Error: Ya existe un estudiante con ese correo'
        
        nuevo = Estudiante(
            nombre=nombre,
            correo=correo,
            carrera=carrera
        )

        #Se envia el objeto al repositorio para guardarlo en la base de datos

        self.repository.registrar(nuevo)
        return 'Estudiante registrado correctamente'
    
    def consultar_estudiante(self):
        return self.repository.consultar_todos()

    def busacr_estudiante(self, id_estudiante):
        return self.repository.busacar_por_id(id_estudiante)

    def actualizar_estudiante(self, id_estudiante, nombre, correo, carrera):
        """
        Actualiza un estudiante despues de validar los datos
        
        :param self: id_estudiante: identificador del estudiamte
        :param nombre: nuevo nombre
        :param correo: nuevo correo
        :param carrera: nueva carrera
        """

        
        nombre = nombre.strip()
        correo = correo.strip()
        carrera = carrera.strip()#club


        #Antes de actualizar se verifica que el estudiante exista
        estudiante_existente = self.repository.busacar_por_id(id_estudiante)
        if estudiante_existente is None:
            return 'Error: No existe un esutidante con ese ID', id_estudiante
        
        #Se crea un objeto estudiante

        nuevo = Estudiante(
        nombre=nombre,
        correo=correo,
        carrera=carrera
        )

        actualizado = self.repository.actualizar(nuevo)

        if actualizado:
            return 'Estudiante actializado correctamente'
        return 'Error no se pudo actualizar el estudiante'
    
    def eliminar_estudiante(self, id_estudiante):
        estudiante_eliminado = self.repository.eliminar(id_estudiante)

        if estudiante_eliminado:
            return 'Estudiante eliminado correctamente'
        return 'Error: No se pudo eliminar el estudiante'
    
