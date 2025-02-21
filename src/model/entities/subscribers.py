from src.model.configs.base import Base
from sqlalchemy import Column,String,Integer, ForeignKey

class Subscribers(Base):
    __tablename__ = "subscribers"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    link = Column(String,nullable=True)
    event_id = Column(Integer, ForeignKey("events.id"))