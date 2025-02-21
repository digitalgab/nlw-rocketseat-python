from abc import ABC, abstractmethod

from src.model.entities.subscribers import Subscribers

class SubscribersRepositoryInterface(ABC):
    @abstractmethod
    def create(self, subscriber_data:dict) -> None: pass
    @abstractmethod  
    def show(self, email:str, event_id: int) -> Subscribers: pass
    @abstractmethod
    def list(self,link:str, event_id:int) -> list:pass
    @abstractmethod
    def show_ranking(self, event_id: int) -> list: pass