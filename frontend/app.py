from flask import Flask
from frontend.view import images


def create_app():
    app = Flask(__name__)

    app.register_blueprint(images.view)

    return app
