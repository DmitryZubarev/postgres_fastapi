from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import db_config
from sqlalchemy_utils import create_database, database_exists


SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://user:password@db-pg:5432/user"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
if not database_exists(SQLALCHEMY_DATABASE_URL):
    create_database(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()