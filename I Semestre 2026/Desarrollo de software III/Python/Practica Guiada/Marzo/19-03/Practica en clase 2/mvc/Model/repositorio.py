class Repositorio:
    def __init__(self):
        self.diccionarioEstudiantes = {}
        self.diccionarioLibros = {}
        self.diccionarioPrestamos = {}

    #Registrar
    def agregarEstudiantes(self, clave, valor):
        self.diccionarioEstudiantes.update({clave: valor})

    def agregarLibros(self, clave, valor):
        self.diccionarioLibros.update({clave: valor})

    def agregarPrestamos(self, clave, valor):
        self.diccionarioPrestamos.update({clave: valor})


    #Consultas
    def consultarEstudiantes(self):
        return self.diccionarioEstudiantes

    def consultarLibros(self):
        return self.diccionarioLibros

    def consultarPrestamos(self):
        return self.diccionarioPrestamos


    #Busquedas personalizadas en el controller