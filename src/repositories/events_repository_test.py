import pytest
from src.model.repositories.events_repository import EventsRepository
from src.model.entities.events import Events
from src.model.configs.connection import DBConnection

@pytest.fixture
def events_repository():
    return EventsRepository()

@pytest.fixture
def event():
    return Events(name="Test Event")

def test_get_all_events(events_repository, event):
    with DBConnection() as db:
        db.session.add(event)
        db.session.commit()
    events = events_repository.get_all_events()
    assert len(events) == 1
    assert events[0].name == "Test Event"

def test_get_event_by_name(events_repository, event):
    with DBConnection() as db:
        db.session.add(event)
        db.session.commit()
    event = events_repository.get_event_by_name("Test Event")
    assert event.name == "Test Event"

def test_create_event(events_repository, event):
    event = events_repository.create_event(event)
    assert event.id is not None

def test_delete_event(events_repository, event):
    with DBConnection() as db:
        db.session.add(event)
        db.session.commit()
    events_repository.delete_event(event)
    with DBConnection() as db:
        event = db.session.query(Events).filter(Events.id == event.id).first()
    assert event is None

def test_update_event(events_repository, event):
    with DBConnection() as db:
        db.session.add(event)
        db.session.commit()
    event.name = "Updated Event"
    events_repository.update_event(event)
    with DBConnection() as db:
        event = db.session.query(Events).filter(Events.id == event.id).first()
    assert event.name == "Updated Event"