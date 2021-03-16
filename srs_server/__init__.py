from flask import Flask

from srs_server.config import config


def register_extension(flask_app: Flask):
    from srs_server import extension
    extension.db.init_app(flask_app)
    extension.jwt.init_app(flask_app)
    # extension.jwt.invalid_token_loader(wrong_token_handler)
    # extension.jwt.expired_token_loader(wrong_token_handler)
    extension.cors.init_app(flask_app)

def register_blueprint(flask_app: Flask):
    from srs_server.view.apply import apply_blueprint
    flask_app.register_blueprint(apply_blueprint)

    from srs_server.view.user import user_blueprint
    flask_app.register_blueprint(user_blueprint)


def create_app(config_name: str) -> Flask:
    flask_app = Flask("SRS_V1")
    flask_app.config.from_object(config[config_name])

    register_blueprint(flask_app)
    register_extension(flask_app)

    return flask_app