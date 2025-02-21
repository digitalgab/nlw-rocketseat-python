from src.interfaces.subscribers_repository import SubscribersRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscribersController:
    def __init__(self, subscriber_repo:SubscribersRepositoryInterface):
        self.__subscriber_repo = subscriber_repo
    
    def create(self, http_request:HttpRequest) -> HttpRequest:
        subscriber_data = http_request.body["data"]
        subscriber_email = subscriber_data["email"]
        event_id = subscriber_data["event_id"]
        
        self.__check(subscriber_email,event_id)
        self.__insert(subscriber_data)
        return self.__format_response(subscriber_data)
        
    def __check(self,subscriber_email:str, event_id:int) -> None:
        response = self.__subscriber_repo.show(email,event_id)
        if response: raise Exception("Subscriber Already Exists!")
        
    def __insert(self,subscriber_data: dict) -> None:
        self.__subscriber_repo.create(subscriber_data)
        
    def __format_response(self,subscriber_data:str) -> HttpResponse:
        return HttpResponse(
            body={
                "data":{
                    "Type":"Subscriber",
                    "count":1,
                    "attributes": subscriber_data
                }
            },
            status_code=201
        )

    def get_subscribers_by_link(self,http_request:HttpRequest) -> HttpRequest:
        link = http_request.param["link"]
        event_id = http_request.param["event_id"]
        subscriber = self.__subscribers_repo.select_subscribers_by_link(link,event_id)
        return self.__format_subscriber_by_link(subscriber)

    def __format_subscriber_by_link(self,subscriber:list) -> HttpResponse:
        return HttpResponse(
            body={
                "data":{
                    "Type":"Subscriber",
                    "count":len(subscriber),
                    "subscribers":subscriber
                }
            },
            status_code=200
        )

    def show_ranking(self,http_request:HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]
        event_ranking = self.__subscribers_repo.show_ranking(event_id)
        return self.__format_event_ranking(event_ranking)s

    def __format_event_ranking(self,event_ranking:list) -> HttpResponse:
        formatted_event_ranking =[]
        for position in event_ranking:
            formatted_event_ranking.append(
                {
                    "link":position.link,
                    "total_subscribers":position.total
                }
            )
        return HttpResponse(
            body={
                "data":{
                    "Type":"Ranking",
                    "count": len(formatted_event_ranking),
                    "ranking": formatted_event_ranking
                }
            },
            status_code=200
        )
    