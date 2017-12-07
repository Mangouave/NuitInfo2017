from flask import Flask, g
from app.event.controllers import blueprint as event

app = Flask(__name__)

app.register_blueprint(event)