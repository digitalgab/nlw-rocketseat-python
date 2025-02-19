from flask import Blueprint, jsonify

event_route = Blueprint("event_route", __name__)

@event_route.route("/events", methods=["GET"])
def list():
    return jsonify({"message": "Events returned"}), 200
@event_route.route("/event", methods=["POST"])
def create():
    return jsonify({"message": "Event created"}), 201

    