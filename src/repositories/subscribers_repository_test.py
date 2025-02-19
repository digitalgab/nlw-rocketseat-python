import pytest
from src.model.configs.connection import DBConnection
from src.model.entities.Subscribers import Subscribers
from src.repositories.subscribers_repository import SubscribersRepository

@pytest.fixture
def subscribers_repository():
    return SubscribersRepository()

def test_create_subscriber(subscribers_repository):
    subscriber_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "event_id": 1
    }
    subscriber = subscribers_repository.create(subscriber_data)
    assert subscriber.name == subscriber_data["name"]
    assert subscriber.email == subscriber_data["email"]
    assert subscriber.event_id == subscriber_data["event_id"]

def test_show_subscriber(subscribers_repository):
    
    subscriber_data = {
        "email": "john.doe@example.com",
        "event_id": 1
    }

    found_subscriber = subscribers_repository.show(subscriber_data["email"], subscriber_data["event_id"])
    assert found_subscriber is not None
    assert found_subscriber.email == subscriber_data["email"]
    assert found_subscriber.event_id == subscriber_data["event_id"]