class Prestamo:
    def __init__(self):
        self.diccionario = {}

    def agregar(self, clave, valor):
        self.diccionario.update({clave: valor})

    def consultar(self):
        return self.diccionario

    def consultarClave(self, clave):
        if clave not in self.diccionario:
            return "No se encontraron datos"
        else:
            return self.diccionario[clave]
        
    def eliminar(self, clave):
        if clave not in self.diccionario:
            return "No se encontraron datos"
        else:
            del self.diccionario[clave]
            return "Eliminado con exito"
    
    def modificar(self, clave, nuevoValor):
        if clave not in self.diccionario:
            return "No se encontraron datos"
        else:
            self.diccionario[clave] = nuevoValor
            return "Modificado  con exito"