class EquipoService:
    def __init__(self, repository):
        self.repo_categoria = repository

    def guardar(self,codigo, nombre, marca, estado, categoria_id):
        if not codigo.strip() or not nombre.strip() or not marca.strip() or not estado.strip():
            raise ValueError ("Debe ingresar datos")

        if self.repo_categoria.list_id(codigo):
            raise ValueError("Ya existe un categoria con ese codigo")

        return self.repo_categoria.save(codigo, nombre, marca, estado, categoria_id)
#---------------------------------------------------------------------------------------------------------
    def listar(self):
        if self.repo_categoria.get_all() is None:
            raise ValueError("No hay equipos registrados")

        return self.repo_categoria.get_all()
#---------------------------------------------------------------------------------------------------------
    def buscar_id(self,codigo):
        if not codigo.strip():
            raise ValueError("Debe ingresar datos")

        if self.repo_categoria.list_id(codigo) is None:
            raise ValueError("No hay equipos registrados con el codigo ingresado")

        return self.repo_categoria.list_id(codigo)
#---------------------------------------------------------------------------------------------------------
    def actualizar(self,codigo, nombre, marca, estado, categoria_id):
        if not codigo.strip():
            raise ValueError("Debe ingresar datos")

        if self.repo_categoria.list_id(codigo) is None:
            raise ValueError("No hay equipos registrados con el codigo ingresado")

        return self.repo_categoria.update(codigo, nombre, marca, estado, categoria_id)
#---------------------------------------------------------------------------------------------------------
    def eliminar(self,codigo):
        if not codigo.strip():
            raise ValueError("Debe ingresar datos")

        if self.repo_categoria.list_id(codigo) is None:
            raise ValueError("No hay equipos registrados con el codigo ingresado")

        return self.repo_categoria.delete(codigo)
#---------------------------------------------------------------------------------------------------------


