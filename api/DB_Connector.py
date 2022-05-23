import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DATABASE_SERVICE = os.environ.get('DATABASE_SERVICE')
DATABASE_SERVICE_PORT = os.environ.get('DATABASE_SERVICE_PORT')



db_uri = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DATABASE_SERVICE}:{DATABASE_SERVICE_PORT}/{POSTGRES_DB}'


engine = create_engine(db_uri, echo = True)


Sessionmaker = sessionmaker(bind=engine)
session = Sessionmaker()

Base = declarative_base()
