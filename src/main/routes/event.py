from flask import Blueprint, jsonify, request
from src.http_types.http_respone import HttpResponse
from src.http_types.http_request import HttpRequest
from src.validators.create_event import create_event_validator

event_route = Blueprint("event_route", __name__)

@event_route.route("/events", methods=["GET"])
def list():
    http_response = HttpResponse(200, {}, {"message": "List Events"})
    return http_response    

@event_route.route("/event", methods=["POST"])
def create():
    create_event_validator(request)
    http_request = HttpRequest(body=request.json)
    return http_request.body
    