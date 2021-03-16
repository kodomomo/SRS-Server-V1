from flask import Blueprint
from flask_restful import Api

apply_blueprint = Blueprint('apply', __name__, url_prefix='/apply')
api = Api(apply_blueprint)

from .seminar_room import SeminarRoom
api.add_resource(SeminarRoom, '/seminar-room')
