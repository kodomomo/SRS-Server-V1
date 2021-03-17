from flask import request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity

from srs_server.data.model.reservation.member_model import MemberModel
from srs_server.data.model.reservation.reservation_model import ReservationModel
from srs_server.data.model.user.user_model import UserModel
from srs_server.view.base_resource import ApplyResource


class SeminarRoom(ApplyResource):
    def get(self):
        room = request.args.get('room')
        reservation_model = ReservationModel.find_by_room(room) if room else ReservationModel.find_all()
        return {
                   'reservation': [
                       {
                           'reservation_id': x.id,
                           'room': x.room,
                           'time': x.time,
                           'leader': self.generate_user_dict(UserModel.find_by_id(x.user_id)),
                           'member': [
                               self.generate_user_dict(UserModel.find_by_id(member.user_id))
                               for member in MemberModel.find_by_reservation_id(x.id)]
                       } for x in reservation_model
                   ]
               }, 200

    @jwt_required()
    def post(self):
        payload = request.json
        id = get_jwt_identity()
        room = payload['room']
        time = payload['time']
        description = payload['description']
        members = payload['members']

        reservation = ReservationModel(id, room, time, description).apply()
        for member in members:
            if not ReservationModel.can_book(time, member): abort(409)
            MemberModel(member, reservation.id).save()

        return {}, 201

    @jwt_required()
    def delete(self):
        payload = request.json
        id = get_jwt_identity()
        reservation_id = payload['reservation_id']

        reservation = ReservationModel.find_by_id(reservation_id)
        if not reservation or not reservation.user_id == id: abort(401)
        reservation.delete()
        return {}, 200

    def generate_user_dict(self, user):
        user_dict = {}
        user_dict['id'] = user.id
        user_dict['name'] = user.name
        user_dict['number'] = user.number
        return user_dict


class MySeminarRoom(ApplyResource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        return {
                   'reservation': [
                       {
                           'reservation_id': x.id,
                           'reason': x.description,
                           'room': x.room,
                           'time': x.time,
                           'leader': self.generate_user_dict(UserModel.find_by_id(x.user_id)),
                           'member': [
                               self.generate_user_dict(UserModel.find_by_id(member.user_id))
                               for member in MemberModel.find_by_reservation_id(x.id)]
                       } for x in [ReservationModel.find_by_id(i.reservation_id)
                                   for i in MemberModel.find_by_user_id(user_id)] + \
                                  ReservationModel.find_by_user_id(user_id)
                   ]
               }, 200

    def generate_user_dict(self, user):
        user_dict = {}
        user_dict['id'] = user.id
        user_dict['name'] = user.name
        user_dict['number'] = user.number
        return user_dict
