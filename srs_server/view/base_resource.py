from datetime import datetime, timedelta

from flask_restful import Resource


class BaseResource(Resource):
    @staticmethod
    def kst_now():
        return datetime.utcnow() + timedelta(hours=9)


class UserResource(BaseResource):
    pass


class ApplyResource(BaseResource):
    pass