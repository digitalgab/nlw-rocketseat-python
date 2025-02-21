from src.model.configs.base import Base
from sqlalchemy import Column,String,Integer, ForeignKey

class EventsLink(Base):
    __tablename__ = "events_link"
    id = Column(Integer,primary_key=True,autoincrement=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    subscriber_id = Column(Integer, ForeignKey("subscribers.id"))
    link = Column(String,nullable=False)