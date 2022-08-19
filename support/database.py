from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from helpers.support_files import read_env_vars


db_uri = read_env_vars('DATABASE_URI')
if 'postgresql' not in db_uri:
    db_uri = db_uri.replace('postgres', 'postgresql')

engine = create_engine(db_uri)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# create database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
