from src.model.configs.base import Base
from sqlalchemy import Column,String,Integer
class Events(Base):
    __tablename__ = "Events"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)