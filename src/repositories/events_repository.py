from src.model.configs.connection import DBConnection
from src.model.entities.events import Events

class EventsRepository:
    def get_all_events(self) -> [Events]:
        with DBConnection() as db:
            return db.session.query(Events).all()

    def get_event_by_name(self, event_name: str) -> Events:
        with DBConnection() as db:
            return db.session.query(Events).filter(Events.name == event_name).one_or_none()

    def create_event(self, event: Events) -> Events:
        with DBConnection() as db:
            db.session.add(event)
            db.session.commit()
            return event

    def delete_event(self, event: Events) -> Events:
        with DBConnection() as db:
            db.session.delete(event)
            db.session.commit()
            return event

    def update_event(self, event: Events) -> Events:
        with DBConnection() as db:
            db.session.merge(event)
            db.session.commit()
            return event

