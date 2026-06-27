from sqlalchemy import Integer, String, Column, ForeignKey

class EquiposORM:
    __tablename__ = 'equipos'
    codigo = Column(String(20), primary_key=True)
    nombre = Column(String(100), nullable=True)
    marca = Column(String(50))
    estado = Column(String(30))
    categoria_id = Column(Integer, ForeignKey('categorias.id'))

    def __repr__(self):
        return f'\n{self.codigo} - {self.nombre} - {self.marca} - {self.estado} - {self.categoria_id}\n'
    
    def to_dict(self):
        return {
            'codigo': {self.codigo},
            'nombre': {self.nombre},
            'marca': {self.marca},
            'estado': {self.estado},
            'categoria': {self.estado}
        }


