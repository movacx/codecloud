class Curso: 
    
    idCurso = 0
    def __init__(self, nombreCurso,codigo, profesorAsignado):
        self.nombreCurso = nombreCurso
        self.codigo = codigo
        self.profesorAsignado = profesorAsignado
        Curso.idCurso += 1
        self.id = Curso.idCurso

    #-----------------------GETS-----------------------#  
    def getNombreCurso(self):
        return self.nombreCurso
    
    def getCodigo(self):
        return self.codigo
    
    def getProfesorAsignado(self):
        return self.profesorAsignado 
    
    #-----------------------GETS-----------------------#  
    def setNombreCurso(self,nombreCurso):
        self.nombreCurso = nombreCurso
    
    def setCodigo(self,codigo):
        self.codigo = codigo
    
    def setProfesorAsignado(self,profesorAsignado):
        self.profesorAsignado = profesorAsignado 
    
    #To String

    def __str__(self):
        return f"""
    Nombre: {self.nombreCurso}
    Edad: {self.codigo}
    Grado:  {self.profesorAsignado}
    """

    def mostrarEstudiantes(self):
        return self.nombreCurso, self.codigo, self.profesorAsignado