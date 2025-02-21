from abc import ABC, abstractmethod

from src.model.entities.events import Events

class EventsRepositoryInterface(ABC):
    @abstractmethod
    def create(self, event_name:str) -> None: pass
    @abstractmethod    
    def show(self, event_name:str)-> Events: pass