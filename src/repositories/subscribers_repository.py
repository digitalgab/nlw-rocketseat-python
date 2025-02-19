from src.model.configs.connection import DBConnection
from src.model.entities.Subscribers import Subscribers
from src.interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscribersRepository(SubscribersRepositoryInterface):
    def list(self) -> [Subscribers]:
        with DBConnection() as db:
            return db.session.query(Subscribers).all()

    def show(self, email: str, event_id: int) -> Subscribers:
        with DBConnection() as db:
            return db.session.query(Subscribers).filter(
                Subscribers.email == email, Subscribers.event_id == event_id
                ).one_or_none()

    def create(self, subscriber: dict) -> None:
        with DBConnection() as db:
            subscriber = Subscribers(
                name=subscriber.get("name"),
                email=subscriber.get("email"),
                link=subscriber.get("link"),
                event_id=subscriber.get("event_id")
            )
            db.session.add(subscriber)
            db.session.commit()
            return subscriber
    def update(self, subscriber: Subscribers) -> Subscribers:
        with DBConnection() as db:
            db.session.merge(subscriber)
            db.session.commit()
            return subscriber

    def delete(self, subscriber: Subscribers) -> Subscribers:
        with DBConnection() as db:
            db.session.delete(subscriber)
            db.session.commit()
            return subscriber

