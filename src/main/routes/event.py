from flask import Blueprint, jsonify

event_route = Blueprint("event_route", __name__)

@event_route.route("/event", methods=["POST"])
def create_event():
    return jsonify({"message": "Event created"}), 201
@event_route.route("/events", methods=["GET"])
def get_events():
    return jsonify({"message": "Events returned"}), 200
    