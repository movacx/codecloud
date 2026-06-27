from Repository.repository_mascotas import RepositoryMascota
from Repository.repository_duenos import RepositoryDuenos 

class ServiceMascota:
    def __init__(self):
        self.repo = RepositoryMascota()
        self.repo_dueno = RepositoryDuenos()
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def registrar_mascota(self, codigo,nombre,especie,edad,dueno_id):
        if not codigo.strip() or not nombre.strip() or not especie.strip():
            raise ValueError('Debe de completar los campos vacios.')
        
        if edad < 1:
            raise ValueError('La edad no puede ser negativa')
        
        if dueno_id < 1:
            raise ValueError('El id dueño no puede ser negativo')

        if self.repo.get_list(codigo):
            raise ValueError(f'Ya existe una mascota asociada al codigo ingresado: {codigo}')
        
        if self.repo_dueno.search_id(dueno_id) is None:
            raise ValueError('No se encontro ningun dueño para registrar la mascota')
        
        return self.repo.save(codigo,nombre,especie,edad,dueno_id)
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def listrar_mascotas(self):
        return self.repo.list()
    
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def buscar_mascotas(self, codigo):
        if not codigo.strip():
            raise ValueError('Debe de completar los campos')
        
        mascota_encontrada = self.repo.get_list(codigo)
        if mascota_encontrada is None:
            raise ValueError(f'No se encontro ninguna mascota asociada al siguiente codigo: {codigo}')
        return mascota_encontrada
    
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def actualizar_mascota(self, codigo, nombre, especie, edad, dueno_id):
        if not codigo.strip() or not nombre.strip() or not especie.strip():
            raise ValueError('Debe de completar los campos vacios.')
        if edad < 1:
            raise ValueError('La edad no puede ser negativa')
        
        mascota_encontrada = self.repo.get_list(codigo)
        if mascota_encontrada is None:
            raise ValueError(f'No se encontro ninguna mascota: {codigo}')
        return self.repo.update(codigo, nombre, especie, edad, dueno_id)
        
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
        
    def eliminar(self, codigo):
        if not codigo.strip():
            raise ValueError('Debe de completar los campos')

        if self.repo.get_list(codigo) is None:
            raise ValueError('No se encontraron datos')
        return self.repo.delete(codigo)
    