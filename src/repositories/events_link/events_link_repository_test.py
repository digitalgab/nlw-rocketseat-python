import pytest
from src.repositories.events_link.events_link_repository import EventosLinkRepository
@pytest.mark.skip("create in DB")
def test_create_eventos_link():
    event_id = 16
    subs_id = 14
    event_link_repo = EventosLinkRepository()
    
    event_link_repo.create(event_id,subs_id)