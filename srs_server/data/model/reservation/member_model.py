from srs_server.extension import db
from srs_server.data.model.base import BaseMixin


class MemberModel(db.Model, BaseMixin):
    __tablename__ = 'tbl_member'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(255), db.ForeignKey('tbl_user.id', ondelete='CASCADE'), nullable=False)
    reservation_id = db.Column(db.Integer, db.ForeignKey('tbl_reservation.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, user_id, reservation_id):
        self.user_id = user_id
        self.reservation_id = reservation_id

    @staticmethod
    def find_by_reservation_id(reservation_id):
        return MemberModel.query.filter_by(reservation_id=reservation_id).all()
