from Model.libro_model import Libro

class Service:
    def __init__(self, repository):
        self.repo_biblioteca = repository

    def registrar_libro(self, codigo, titulo, autor, categoria):
        if not codigo.strip():
            raise ValueError('El campo es obligatorio')
        if not titulo.strip():
            raise ValueError('El titulo es obligatorio debe de completarlo!')
        if not autor.strip():
            raise ValueError('El autor es obligatorio debe de completarlo!')
        if not categoria.strip():
            raise ValueError('La categoria es obligatorio debe de completarlo!')
        
        # libro_consultado = self.repo_biblioteca.consultar_libro(codigo)

        # if libro_consultado.codigo == codigo:
        #     raise ValueError(f'Ya existe un registro con el mismo codigo: {codigo}')
        
        nuevo_libro = Libro(codigo, titulo, autor, categoria)
        
        exito = self.repo_biblioteca.registrar(nuevo_libro)
        if exito != True:
            return 'Hubo un error, no se pudo registrar el libro'
        else:
            return 'Registrado con exito!'
        

    #=--==--=-==--=-=-=-=--=-=-=-=-==-=-=-=-=--=-==-=-=-=-=--==-=--=-==--=-=-==-=--==-=-=--=-=-=
    def consultar_libros(self):
        for items in self.repo_biblioteca.consultar_datos():
            print(items)

    def buscar_libro(self, codigo):
        if not codigo.strip():
            raise ValueError('El campo es obligatorio')
        
        return self.repo_biblioteca.consultar_libro(codigo)
    
    def buscar_categoria(self, categoria):
        if not categoria.strip():
            raise ValueError('La categoria es obligatorio debe de completarlo!')
        
        return self.repo_biblioteca.filtrar_categoria(categoria)
    
    
        
