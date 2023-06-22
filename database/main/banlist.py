from sqlalchemy import Column, Integer, Boolean
from database.main import Base


class Banlist(Base):
    __tablename__ = 'banlist'
    telegram_id = Column(Integer, primary_key=True)