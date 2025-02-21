from flask import Blueprint,jsonify, request
from src.http_types.http_request import HttpRequest
from src.validators.create_subscriber import create_subscribers_validator
from src.repositories.subscribers_repository import SubscribersRepository
from src.controllers.subscribers_controller import SubscribersController

subscribers_route_bp =Blueprint("subscribers_route",__name__)
@subscribers_route_bp.route("/subscriber",methods=["POST"])

def create():
    create_subscribers_validator(request)
    http_request = HttpRequest(body=request.json)
    
    subscribers_repo = SubscribersRepository()
    subscriber_controller = SubscribersController(subscribers_repo)
    http_response = subscriber_controller.create(http_request)

    return jsonify(http_response.body),http_response.status_code

@subscribers_route_bp.route("/subscriber/link/<link>/event/<event_id>", methods=["GET"])
def subscribers_by_link(link, event_id):
    subscribers_repo = SubscribersRepository()
    subscriber_controller = SubscribersController(subscribers_repo)

    http_request = HttpRequest(param={ "link": link, "event_id": event_id })

    http_response = subscriber_controller.get_subscribers_by_link(http_request)

    return jsonify(http_response.body), http_response.status_code
#ranking
@subscribers_route_bp.route("/subscriber/ranking/event/<event_id>", methods=["GET"])
def show_ranking(event_id):
    subscribers_repo = SubscribersRepository()
    subscriber_controller = SubscribersController(subscribers_repo)

    http_request = HttpRequest(param={ "event_id": event_id })
    http_response = subscriber_controller.show_ranking(http_request)

    return jsonify(http_response.body), http_response.status_code