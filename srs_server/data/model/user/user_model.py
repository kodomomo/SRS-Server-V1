from srs_server.extension import db
from srs_server.data.model.base import BaseMixin


class UserModel(db.Model, BaseMixin):
    __tablename__ = 'tbl_user'
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(4), nullable=False)
    number = db.Column(db.String(4), nullable=False)

    def __init__(self, id, name, number):
        self.id = id
        self.name = name
        self.number = number

    @staticmethod
    def signup  (oauth, identity, name, number):
        return UserModel(f"{oauth}@{identity}", name, number).save()

    @staticmethod
    def signin(oauth, identity):
        id = f"{oauth}@{identity}"
        return UserModel.query.filter_by(id=id).first()

    @staticmethod
    def find_by_id(id):
        return UserModel.query.filter_by(id=id).first()

    @staticmethod
    def search_by_number(number):
        print(type(number))
        return UserModel.query.filter(UserModel.number.like(f'%{number}%')).all()
