from abc import ABC, abstractmethod
from src.model.entities.subscribers import Subscribers

class SubscribersRepositoryInterface(ABC):
    @abstractmethod
    def list(self) -> [Subscribers]:
        raise NotImplementedError
    def show(self, email: str, event_id: int) -> Subscribers:
        raise NotImplementedError
    @abstractmethod
    def create(self, subscriber: dict) -> None:
        raise NotImplementedError
    @abstractmethod
    def update(self, subscriber: Subscribers) -> Subscribers:
        raise NotImplementedError
    @abstractmethod
    def delete(self, subscriber: Subscribers) -> Subscribers:
        raise NotImplementedError
