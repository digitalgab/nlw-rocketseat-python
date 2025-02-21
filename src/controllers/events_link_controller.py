from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.interfaces.events_link_repository import EventsLinkRepositoryInterface

class EventsLinkController:
    def __init__(self,events_link_repo:EventsLinkRepositoryInterface):
        self.__events_link_repo = events_link_repo
        
    def create(self,http_request:HttpRequest) -> HttpResponse:
        event_link = http_request.body["data"]
        event_id = event_link["event_id"]
        subscriber_id = event_link["subscriber_id"]
        
        self.__check(event_id,subscriber_id)
        event_link = self.__create(event_id,subscriber_id)
        return self.__format_response(event_link,event_id,subscriber_id)
    
    def __check(self,event_id:int,subscriber_id:int) ->None:
        response = self.__events_link_repo.select_events_link(event_id,subscriber_id)
        if response: raise Exception("Link Already Exists!")
    
    def __create(self, event_id:int,subscriber_id:int) -> str:
        event_link = self.__events_link_repo.create(event_id,subscriber_id)
        return event_link
    
    def __format_response(self,event_link:str,event_id:int,subscriber_id:int)-> HttpResponse:
        return HttpResponse(
            body={
                "data":{
                    "Type": "Event Link",
                    "count":1,
                    "attributes":{
                        "link":event_link,
                        "event_id":event_id,
                        "subscriber_id":subscriber_id
                    }
                }
            },
            status_code=201
        )