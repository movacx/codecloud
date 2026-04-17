from Model.estudianteModel import Estudiante

class EstudianteService:
    def __init__(self, repo):
        self.repo = repo

    def registro_estudiante(self, carnet, nombre, carrera):
        if not carnet.strip():
            raise ValueError('El carnet es obligatorio')
        if not nombre.strip():
            raise ValueError('El nombre es obligatorio')
        if not carrera.strip():
            raise ValueError('La carrera es obligatoria')

        if self.buscar_estudiante(carnet):
            raise ValueError('No pueden haber dos estudiantes con el mismo numero de carnet')


        nuevo_estudiante = Estudiante(carnet, nombre, carrera)
        exito =  self.repo.agregar(nuevo_estudiante)
        if exito:
            return True
        else:
            return False

    def mostrar_estudiantes(self):
        return self.repo.mostrar_todo()

    def buscar_estudiante(self, carnet):
        if not carnet.strip():
            raise ValueError('El carnet es obligatorio')
        return self.repo.buscar_estudiante(carnet)
