class Curso: 
    idCurso = 0
    def __init__(self, nombreCurso, codigo, profesorAsignado):
        self.nombreCurso = nombreCurso
        self.codigo = codigo
        self.profesorAsignado = profesorAsignado
        
        Curso.idCurso += 1
        self.id = Curso.idCurso

    # Getters
    def getNombreCurso(self):
        return self.nombreCurso
    def getCodigo(self):
        return self.codigo
    def getProfesorAsignado(self):
        return self.profesorAsignado 
    
    # Setters
    def setNombreCurso(self, nombreCurso):
        self.nombreCurso = nombreCurso
    def setCodigo(self, codigo):
        self.codigo = codigo
    def setProfesorAsignado(self, profesorAsignado):
        self.profesorAsignado = profesorAsignado 
    
    def mostrarDatos(self):
        return f"[ID: {self.id}] Curso: {self.nombreCurso} | Código: {self.codigo} | Profesor: {self.profesorAsignado}"