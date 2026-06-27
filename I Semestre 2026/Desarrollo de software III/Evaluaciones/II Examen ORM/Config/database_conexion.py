from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

URL_BASE = 'mysql+pymysql://root:Skull_fab%4019@localhost:3306/videojuegos_db'

engine = create_engine(URL_BASE, echo=False)
LocalSession = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
    from Entity.fileVideojuegos import VideoJuegoORM
    from Entity.fileJugadores import JugadoresORM
    Base.metadata.create_all(bind=engine)


