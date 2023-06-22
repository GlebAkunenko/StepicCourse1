import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeMeta

load_dotenv()


engine = create_engine(f'sqlite:///{os.getenv("DATABASE_NAME")}.sqlite')
session = sessionmaker(bind=engine)()

Base: DeclarativeMeta = declarative_base()


def create():
    Base.metadata.create_all(engine)
