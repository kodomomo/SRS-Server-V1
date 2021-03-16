from flask import request, abort
from flask_jwt_extended import create_access_token

from srs_server.data.model.user.user_model import UserModel
from srs_server.data.requests.ddyzd import DDYZDService
from srs_server.view.base_resource import UserResource


class Auth(UserResource):
    def post(self):
        payload = request.json

        if payload['auth_type'] == "ddyzd":
            inform = DDYZDService.get_inform(payload['token'])
            print(inform)
            if not UserModel.signin("ddyzd", inform['email']):
                UserModel.signup("ddyzd", inform["email"], inform["name"], inform["gcn"])
        else:
            abort(403)

        return {
            "access_token": create_access_token(identity=f"{payload['auth_type']}@{inform['email']}")
               }, 200