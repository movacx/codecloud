from Repository.jugador_repository import JugadorRepository
class JugadorService:
    def __init__(self):
        self.repo = JugadorRepository()
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def agregar(self, identificacion,nombre_completo,correo_electronico,pais):
        if not identificacion.strip() or not nombre_completo.strip() or not correo_electronico.strip() or not pais.strip():
            raise ValueError('Debe de completar los espacios vacios')
        if self.repo.list_id(identificacion):
            raise ValueError('El id ingresado ya existe')
        if '@' not in correo_electronico:
            raise ValueError('es necesario ingresar una direccion valida {ejemplo: @gmail.com}')

        return self.repo.save(identificacion,nombre_completo,correo_electronico,pais)
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def mostrar(self):
        dato_encontrado = self.repo.list()
        if dato_encontrado is None:
            raise ValueError('No se encontraron datos')
        return dato_encontrado
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def buscar(self,identificacion):
        dato_encontrado = self.repo.list_id(identificacion)
        if dato_encontrado is None:
            raise ValueError(f'No se encontro ningun jugador asociado al siguiente ID: {identificacion}')
        return dato_encontrado
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def filtrar_categoria(self, categoria):
        dato_encontrado = self.repo.list_id(categoria)
        if dato_encontrado is None:
            raise ValueError(f'No se encontro ninguna categoria: {categoria}')
        return dato_encontrado
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def filtrar_pais(self, pais):
        dato_encontrado = self.repo.list_country(pais)
        if dato_encontrado is None:
            raise ValueError(f'No se encontro ningun pais con el nombre: {pais}')
        return dato_encontrado