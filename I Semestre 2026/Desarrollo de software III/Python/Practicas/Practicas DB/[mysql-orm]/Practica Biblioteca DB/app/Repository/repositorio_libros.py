from Config.database_conexion import SessionLocal
from Entity.biblioteca import LibroORM



class LibroRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create(self, codigo,titulo,categoria,anio_publicacion,autor_id):
        libro = LibroORM(codigo=codigo,titulo=titulo,categoria=categoria,anio_publicacion=anio_publicacion,autor_id=autor_id)
        self.db.add(libro)
        self.db.commit()
        return libro
    
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def get_all(self):
        return self.db.query(LibroORM).all()
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def get_codigo(self, codigo):
        return self.db.query(LibroORM).filter_by(codigo=codigo).first()
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def update(self, codigo,titulo,categoria,anio_publicacion,autor_id):
        libro = self.get_codigo(codigo)
        if libro:
            libro.titulo = titulo
            libro.categoria = categoria
            libro.anio_publicacion = anio_publicacion
            libro.autor_id = autor_id
            self.db.commit()
        return libro
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def delete(self, codigo):
        libro = self.get_codigo(codigo)
        if libro:
            self.db.delete(libro)
            self.db.commit()
        return libro
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def filtrar_por_categoria(self, categoria: str):
        return self.db.query(LibroORM).filter(LibroORM.categoria == categoria).all()

    def get_by_autor_id(self, autor_id):
        return self.db.query(LibroORM).filter(LibroORM.autor_id == autor_id).all()

    def get_titulos_asc(self):
        return self.db.query(LibroORM).order_by(LibroORM.titulo).all()
    
    
    # codigo = Column(String(20), primary_key=True)
    # titulo = Column(String(100), nullable=False)
    # categoria = Column(String(50))
    # anio_publicacion = Column(Integer)
    # autor_id = Column(Integer, ForeignKey('autores.id'))

