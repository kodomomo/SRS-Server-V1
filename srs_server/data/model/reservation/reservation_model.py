from flask import abort

from srs_server.extension import db
from srs_server.data.model.base import BaseMixin


class ReservationModel(db.Model, BaseMixin):
    __tablename__ = 'tbl_reservation'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(255), db.ForeignKey('tbl_user.id', ondelete='CASCADE'), nullable=False)
    room = db.Column(db.String(3), nullable=False)
    time = db.Column(db.String(6), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __init__(self, user_id, room, time, description):
        self.user_id = user_id
        self.time = time
        self.room = room
        self.description = description

    @staticmethod
    def find_by_room_and_time(room, time):
        return ReservationModel.query.filter_by(room=room).filter_by(time=time).first()

    def apply(self):
        if ReservationModel.find_by_room_and_time(self.room, self.time): abort(409)
        return self.save()

    @staticmethod
    def find_all():
        return ReservationModel.query.all()

    @staticmethod
    def find_by_id(id):
        return ReservationModel.query.filter_by(id=id).first()

