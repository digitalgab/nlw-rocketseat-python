import pytest
from src.repositories.events.events_repository import EventsRepository

@pytest.mark.skip("create in DB")
def test_create_Events():
    event_name = "event2"
    event_repo = EventsRepository()

    
    event_repo.create(event_name)
    
@pytest.mark.skip("show in DB") 
def test_show_event():
    event_name = "event2"
    event_repo = EventsRepository()    
    event = event_repo.show(event_name)
