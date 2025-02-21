from abc import ABC,abstractmethod

from src.model.entities.events_link import EventsLink

class EventsLinkRepositoryInterface(ABC):
    @abstractmethod
    def create(self, event_id:int, subscriber_id:int) -> str: pass
    
    @abstractmethod  
    def show(self, event_id:int, subscriber_id:int)-> EventsLink: pass