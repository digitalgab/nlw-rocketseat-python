from flask import Flask
from src.main.routes.event import event_route
from src.main.routes.subscribers import subscribers_route
from src.main.routes.events_link import event_link_route

app = Flask(__name__)
app.register_blueprint(event_route)
app.register_blueprint(subscribers_route)
app.register_blueprint(event_link_route)    