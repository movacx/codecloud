from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

URL_BASE = 'mysql+pymysql://root:Skull_fab%4019@localhost:3306/clinica_veterinaria_db'

engine = create_engine(URL_BASE, echo = False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def init_db():
    from Entity.duenosORM import DuenosOrm
    from Entity.mascotasORM import MascotasORM
    Base.metadata.create_all(bind=engine)