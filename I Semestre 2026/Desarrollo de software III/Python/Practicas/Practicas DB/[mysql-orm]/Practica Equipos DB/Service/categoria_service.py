class CategoriaService:
    def __init__(self, repository):
        self.repo_categoria = repository

    def guardar(self,id, nombre):

        if not id.strip() or not nombre.strip():
            raise ValueError("Debe ingresar un dato")

        if self.repo_categoria.list_id(id):
            raise ValueError("El dato ya existe")

        return self.repo_categoria.save(id, nombre)
#---------------------------------------------------------------------------------------------------------
    def listar(self):
        if self.repo_categoria.get_all() is None:
            raise ValueError("No hay categorias a mostrar")

        return self.repo_categoria.get_all()
#---------------------------------------------------------------------------------------------------------
    def buscar_id(self,id):
        if not id.strip():
            raise ValueError("Debe ingresar un dato")

        categoria_encontrada = self.repo_categoria.list_id(id)
        if categoria_encontrada is None:
            raise ValueError("No existe ninguna categoria con ese ID")

        return categoria_encontrada
#---------------------------------------------------------------------------------------------------------
    def actualizar(self, id, nombre):
        if not id.strip() or not nombre.strip():
            raise ValueError("Debe ingresar un dato")

        if self.repo_categoria.list_id(id) is None:
            raise ValueError("No existe ninguna categoria con ese ID")

        return self.repo_categoria.update(id, nombre)
#---------------------------------------------------------------------------------------------------------
    def eliminar(self, id):
        if not id.strip():
            raise ValueError("Debe ingresar un dato")

        if self.repo_categoria.list_id(id) is None:
            raise ValueError("No existe ninguna categoria con ese ID")

        return self.repo_categoria.delete(id)
#---------------------------------------------------------------------------------------------------------


