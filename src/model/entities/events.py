from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.model.configs.base import Base

class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

def __init__(self, name):
    self.name = name