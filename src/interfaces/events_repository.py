from abc import ABC, abstractmethod
from src.model.entities.events import Events

class EventsRepositoryInterface(ABC):
    @abstractmethod
    def list(self) -> [Events]:
        raise NotImplementedError

    @abstractmethod
    def show(self, event_name: str) -> Events:
        raise NotImplementedError

    @abstractmethod
    def create(self, event_name: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, event: Events) -> Events:
        raise NotImplementedError

    @abstractmethod
    def delete(self, event: Events) -> Events:
        raise NotImplementedError

