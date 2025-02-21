from flask import Blueprint,jsonify, request

event_link_route_bp =Blueprint("event_link_route",__name__)

from src.http_types.http_request import HttpRequest
from src.controllers.events_controller import EventsLinkController

from src.model.repositories.events_link_repository import EventsLinkRepository

@event_link_route_bp.route("/events-link",methods=["POST"])

def create():
    events_link_repo = EventsLinkRepository()
    events_link_controller = EventsLinkController(events_link_repo)
    
    http_request = HttpRequest(body=request.json)
    http_response = events_link_controller.create(http_request)
    return jsonify(http_response.body),http_response.status_code