from Entity.biblioteca import LibroORM
from Repository.repositorio_libros import LibroRepository
from Service.service_autor import ServiceAutor

class ServiceLibro:
    def __init__(self):
        self.repo = LibroRepository()
        self.service_autor = ServiceAutor()


    def create_libro(self, codigo,titulo,categoria,anio_publicacion,autor_id):
        if not codigo.strip() or not titulo.strip() or not categoria.strip() or not anio_publicacion.strip() or not autor_id.strip():
            raise ValueError('Debe de completar los campos vacios')
        
        if self.service_autor.get_autor(autor_id) is None:
            raise ValueError(f'No se encontro ningun autor con el siguiente id: {autor_id}')
        
        if self.repo.get_codigo(codigo):
            raise ValueError(f'Ya existe un libro registrado con el siguiente codigo: {codigo}')

        return self.repo.create(codigo,titulo,categoria,anio_publicacion,autor_id)
    
    #-=-=-=-=-==-=--=-=-=-==--==-=-=-=-=-=-=-=--==--=-=-=-=-=-=-==-=-=--==-=-=-=--==--==-=-=-=--#
    def get_libros(self):
        return self.repo.get_all()
    #-=-=-=-=-==-=--=-=-=-==--==-=-=-=-=-=-=-=--==--=-=-=-=-=-=-==-=-=--==-=-=-=--==--==-=-=-=--#
    def get_libro_codigo(self, codigo):
        if not codigo.strip():
            raise ValueError('El campo no puede quedar vacio')
        
        return self.repo.get_codigo(codigo)
    #-=-=-=-=-==-=--=-=-=-==--==-=-=-=-=-=-=-=--==--=-=-=-=-=-=-==-=-=--==-=-=-=--==--==-=-=-=--#
    def update_libro(self, codigo,titulo,categoria,anio_publicacion,autor_id):
        if not codigo.strip() or not titulo.strip() or not categoria.strip() or not anio_publicacion.strip() or not autor_id.strip():
            raise ValueError('Debe de completar los campos vacios')
        
        if self.repo.get_codigo(codigo) is None:
            raise ValueError(f'No se encontro ningun libro con el siguiente codigo: {codigo}')
        
        return self.repo.update(codigo,titulo,categoria,anio_publicacion,autor_id)
    #-=-=-=-=-==-=--=-=-=-==--==-=-=-=-=-=-=-=--==--=-=-=-=-=-=-==-=-=--==-=-=-=--==--==-=-=-=--#
    def delete_libro(self, codigo):
        if not codigo.strip():
            raise ValueError('Debe de completar el campo vacio')
        
        if self.repo.get_codigo(codigo) is None:
            raise ValueError(f'No se encontro ningun libro con el siguiente codigo: {codigo}')
        
        return self.repo.delete(codigo)
    
    #-=-=-=-==--=-=-==-=-=-=-=-=[Esto es para el reportes]-=-=-=-=--=-==-=-=-=-=-=-=-=-=-=-=-=-=-
    
    # def filtrar_categorias(self, categoria):
    #     if not categoria.strip():
    #         raise ValueError('El campo no puede quedar vacio')
        
    #     resultado = []
    #     datos = self.repo.get_all()
    #     for items in datos:
    #         if items:
    #             if items.categoria == categoria:
    #                 resultado.append(items)
    #     return resultado

    def ordenar_titulos(self):
        return self.repo.get_titulos_asc()

    def filtrar_autor_por_libro(self, nombre_autor):
        if not nombre_autor.strip():
            raise ValueError('El campo no puede quedar vacio')
        
        autor = self.service_autor.buscar_nombre(nombre_autor)
        if not autor:
            raise ValueError('No se encontro ningun autor relacionado')
        
        return self.repo.get_by_autor_id(autor.id)


    def filtrar_categoria_mejorada(self, categoria):
        if not categoria.strip():
            raise ValueError('Complete el bendito espacio')
        
        return self.repo.filtrar_por_categoria(categoria)
