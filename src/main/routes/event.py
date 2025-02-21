from flask import Blueprint,jsonify, request

event_route_bp =Blueprint("event_route",__name__)

from src.validators.create_event import events_creator_validator
from src.http_types.http_request import HttpRequest
from src.controllers.events.events_controller import EventsController
from src.model.repositories.eventos_repository import EventosRepository

@event_route_bp.route("/event",methods=["POST"])

def create():
    events_creator_validator(request)
    http_request = HttpRequest(body=request.json)
    
    eventos_repo = EventosRepository()
    events_controller = EventsController(eventos_repo)
    http_response = events_controller.create(http_request)
    
    return jsonify(http_response.body),http_response.status_code