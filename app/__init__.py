from flask import Flask
from flask_cors import CORS
from .routes import configure_routes

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/translate": {"origins": "*"}})

    configure_routes(app)  # Configura as rotas

    return app
