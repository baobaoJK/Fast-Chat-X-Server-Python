from flask_socketio import SocketIO
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
