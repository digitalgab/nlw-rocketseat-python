from src.model.configs.connection import DBConnection
from src.model.entities.events import Events
from src.interfaces.events_repository import EventsRepositoryInterface

class EventsRepository(EventsRepositoryInterface):
    def list(self) -> [Events]:
        with DBConnection() as db:
            return db.session.query(Events).all()

    def show(self, event_name: str) -> Events:
        with DBConnection() as db:
            return db.session.query(Events).filter(Events.name == event_name).one_or_none()

    def create(self, event_name: str) -> None:
        with DBConnection() as db:
            event = Events(name=event_name)
            db.session.add(event)
            db.session.commit()
            return event
    def update(self, event: Events) -> Events:
        with DBConnection() as db:
            db.session.merge(event)
            db.session.commit()
            return event

    def delete(self, event: Events) -> Events:
        with DBConnection() as db:
            db.session.delete(event)
            db.session.commit()
            return event

