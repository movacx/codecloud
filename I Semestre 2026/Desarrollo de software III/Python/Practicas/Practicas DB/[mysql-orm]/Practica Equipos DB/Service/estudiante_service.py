class EstudianteService:
    def __init__(self, repository):
        self.repo_estudiantes = repository

    def guardar(self, id, nombre, correo, carrera):
        if not id.strip() or not nombre.strip() or not correo.strip() or not carrera.strip():
            raise ValueError("Debe ingresar datos")

        if self.repo_estudiantes.list_id(id):
            raise ValueError("Estudiante ya existe")

        return self.repo_estudiantes.save(id, nombre, correo, carrera)
#---------------------------------------------------------------------------------------------------------
    def listar(self):
        if self.repo_estudiantes.get_all() is None:
            raise ValueError("Error! No existen estudiantes")

        return self.repo_estudiantes.get_all()
#---------------------------------------------------------------------------------------------------------
    def buscar_id(self,id):
        if not id.strip():
            raise ValueError("Debe ingresar datos")

        if self.repo_estudiantes.list_id(id) is None:
            raise ValueError("Error! No se encontro estudiante con el ID ingresado")

        return self.repo_estudiantes.list_id(id)
#---------------------------------------------------------------------------------------------------------
    def actualizar(self, id, nombre, correo, carrera):
        if not id.strip() or not nombre.strip() or not correo.strip() or not carrera.strip():
            raise ValueError("Debe ingresar datos")

        if self.repo_estudiantes.list_id(id) is None:
            raise ValueError("Error! No se encontro estudiante con el ID ingresado")

        return self.repo_estudiantes.update(id, nombre, correo, carrera)
#---------------------------------------------------------------------------------------------------------
    def eliminar(self, id):
        if not id.strip():
            raise ValueError("Debe ingresar datos")

        if self.repo_estudiantes.list_id(id) is None:
            raise ValueError("Error! No se encontro estudiante con ID ingresado")
#---------------------------------------------------------------------------------------------------------


