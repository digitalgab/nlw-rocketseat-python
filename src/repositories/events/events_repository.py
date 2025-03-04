from src.model.configs.connection import DBConnectionHandler
from src.model.entities.events import Events
from .interfaces.events_repository import EventsRepositoryInterface

class EventsRepository(EventsRepositoryInterface):
    def create(self, event_name:str) -> None:
        with DBConnectionHandler() as db:
            try:
                event = Events(nome=event_name)
                db.session.add(event)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def show(self, event_name:str)-> Events:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Events)
                .filter(Events.nome == event_name)
                .one_or_none()
            )
            return data