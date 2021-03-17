from flask import request, abort

from flask_jwt_extended import jwt_required, get_jwt_identity

from srs_server.data.model.user.user_model import UserModel
from srs_server.data.requests.ddyzd import DDYZDService
from srs_server.view.base_resource import UserResource


class User(UserResource):
    @jwt_required()
    def get(self):
        id = get_jwt_identity()
        user = UserModel.find_by_id(id)
        return {
            "id": user.id,
            "name": user.name,
            "number": user.number
        }, 200

    def post(self):
        payload = request.json

        if payload['auth_type'] == "ddyzd":
            inform = DDYZDService.get_inform(payload['token'])
            UserModel.signup("ddyzd", inform['email'], inform['name'], inform['gcn'])
        else:
            abort(407)

        return {}, 201


class Search(UserResource):
    def get(self):
        number = request.args.get('number')
        users = UserModel.search_by_number(number)
        return {'users': [self.generate_user_dict(user) for user in users]}, 200

    def generate_user_dict(self, user):
        user_dict = {}
        user_dict['id'] = user.id
        user_dict['name'] = user.name
        user_dict['number'] = user.number
        return user_dict
