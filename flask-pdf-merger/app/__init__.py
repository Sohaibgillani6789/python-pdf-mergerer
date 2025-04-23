from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='your_secret_key_here',
    )

    with app.app_context():
        from . import routes

    return app