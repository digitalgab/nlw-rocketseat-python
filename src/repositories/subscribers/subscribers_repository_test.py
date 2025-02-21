import pytest
from src.repositories.subscribers.subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_create():
    subscriber={
        "name":"João",
        "email":"j@email.com",
        "evento_id":4
    }
    subscribe_repo = SubscribersRepository()
    subscribe_repo.create(subscriber)
@pytest.mark.skip("Select in DB")
def test_select_subscriber():
    email = "a@email.com"
    evento_id = 3
    
    subscribe_repo = SubscribersRepository()
    resp = subscribe_repo.select_subscriber(email,evento_id)

@pytest.mark.skip("Select ranking in DB")
def test_ranking():
    evento_id = 3
    subscribe_repo = SubscribersRepository()
    resp = subscribe_repo.show_ranking(evento_id)

    for elem in resp:
        print(f"Link: {elem.link}, total de inscritos: {elem.total}")