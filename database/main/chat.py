from sqlalchemy import Column, Integer, Boolean
from database.main import Base


class Chat(Base):
    __tablename__ = 'chat'

    chat_id = Column(Integer, primary_key=True)

    def __repr__(self) -> str:
        return f'Chat {self.chat_id}'