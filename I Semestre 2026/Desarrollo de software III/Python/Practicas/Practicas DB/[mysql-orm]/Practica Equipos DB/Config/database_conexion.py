from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

BASE_URL = 'mysql+pymysql://root:Skull_fab%4019@localhost:3306/prestamos_equipos_db'

engine = create_engine(BASE_URL, echo=False)
SessionLocal = sessionmaker(bind = engine)

Base = declarative_base()

def init_db():
    from Entity.categoriasORM import CategoriasORM
    from Entity.equiposORM import EquiposORM
    from Entity.estudiantesORM import EstudianteORM
    from Entity.prestamosORM import PrestamosORM
    Base.metadata.create_all(bind=engine)