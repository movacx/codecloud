from Repository.repositorio_autor import AutorRepository

class ServiceAutor:
    def __init__(self):
        self.repo = AutorRepository()

    def create_autor(self,nombre,nacionalidad):
        if not str(nombre).strip() or not nombre.strip() or not nacionalidad.strip():
            raise ValueError('El campo no puede estar vacio')
        
        if self.repo.get(id):
            raise ValueError('Ya existe un autor con el mismo id')
        
        autor = self.repo.create(nombre,nacionalidad)

        return True, autor #retorno el autor para imprimirlo despues.
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def list_all(self):
        return self.repo.get_all()
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def get_autor(self, id):
        if not str(id).strip():
            raise ValueError('El campo no puede estar vacio')
        
        encontrado = self.repo.get(id)
        if not encontrado:
            raise ValueError(f'No se encontro ningun autor con el id: {id}')
        
        return encontrado
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def update_autor(self, id, nombre, nacionalidad):
        if not str(id).strip() or not nombre.strip() or not nacionalidad.strip():
            raise ValueError('El campo no puede estar vacio')
        
        if self.repo.get(id) is None:
            raise ValueError(f'No se encontro ningun autor con el id: {id}')
        
        return self.repo.update(id,nombre,nacionalidad)
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def delete_autor(self, id):
        if not str(id).strip():
            raise ValueError('El campo no puede estar vacio')
        
        if self.repo.get(id) is None:
            raise ValueError(f'No se encontro ningun autor con el id: {id}')
        
        return self.repo.delete(id)
    
    def buscar_nombre(self, nombre):
        if not nombre.strip():
            raise ValueError('Campo esta vacio')
        autor = self.repo.get_por_nombre(nombre)
        return autor
    
    def filtrar_nacionalidad(self, nacionalidad):
        if not nacionalidad.strip():
            raise ValueError('El campo no puede quedar vacio')
        
        return self.repo.get_nacionalidad(nacionalidad)