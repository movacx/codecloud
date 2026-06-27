from Repository.repository_duenos import RepositoryDuenos
from Repository.repository_mascotas import RepositoryMascota


class ServiceDuenos:
    def __init__(self):
        self.repo_duenos = RepositoryDuenos()
        self.repo_mascota = RepositoryMascota()
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def registrar_duenos(self, nombre,telefono,email):
        if not nombre.strip() or not telefono.strip() or  not email.strip():
            raise ValueError('El campo no puede quedar vacio')
        
        tupla = (nombre,telefono,email)


        return self.repo_duenos.save(tupla)
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def listar_duenos(self):
        datos_encontrados = self.repo_duenos.get_all()
        if datos_encontrados is None:
            raise ValueError('No se encontraron datos')
        return datos_encontrados
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def buscar_duenos(self, nombre):
        datos_encontrados = self.repo_duenos.search_name(nombre)
        if datos_encontrados is None:
            raise ValueError('No se encontraron datos')
        
        return self.repo_duenos.search_name(nombre)
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def actualizar_duenos(self, id, nombre,telefono,email):
        if not nombre.strip() or not telefono.strip() or  not email.strip():
            raise ValueError('El campo no puede quedar vacio')
        
        datos_encontrados = self.repo_duenos.search_id(id)
        if datos_encontrados is None:
            raise ValueError('No se encontraron datos')
        
        return self.repo_duenos.update(id,nombre,telefono,email)
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def eliminar(self, id):
        if not id.strip():
            raise ValueError('El campo no puede quedar vacio')

        if self.repo_mascota.existe_dueno_con_mascota(id):
            raise ValueError('No se puede eliminar este dueño porque tiene una mascota asociada')


        datos_encontrados = self.repo_duenos.search_id(id)
        if datos_encontrados is None:
            raise ValueError('No se encontraron datos')
        
        return self.repo_duenos.delete(id)
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#

        
