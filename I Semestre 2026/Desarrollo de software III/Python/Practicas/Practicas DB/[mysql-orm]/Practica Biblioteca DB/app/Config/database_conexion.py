from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = 'mysql+pymysql://root:Skull_fab%4019@localhost:3306/biblioteca_db'

engine = create_engine(DATABASE_URL, echo = False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)