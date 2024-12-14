from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.insert import insertReservation
from Database.Delete import deleteReservation
from Database.Get import getReservation
bp = Blueprint('reservation', __name__, url_prefix='/reservation')

@bp.route('/insert_reservation', methods=['POST'])
@token_required
@role_required('admin')
def insert_reservation():
    data = request.json
    passengerID = data.get('passengerID')
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    firstStation = data.get('firstStation')
    lastStation = data.get('lastStation')
    seat = data.get('seat')
   
    insertReservation(passengerID, tripNumber, date, firstStation, lastStation, seat)

    return jsonify({"Reservation": "Inserted Successfully"})


@bp.route('/get_reservation', methods=['GET'])
@token_required
@role_required('admin')
def get_reservation():
    data = request.json
    passengerID = data.get('passengerID')
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    firstStation = data.get('firstStation')
    lastStation = data.get('lastStation')
   
    reservation = getReservation(passengerID, tripNumber, date, firstStation, lastStation)

    return jsonify({"Reservation": reservation})


@bp.route('/delete_reservation', methods=['POST'])
@token_required
@role_required('admin')
def delete_reservation():
    data = request.json
    passengerID = data.get('passengerID')
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    firstStation = data.get('firstStation')
    lastStation = data.get('lastStation')
   
    deleteReservation(passengerID, tripNumber, date, firstStation, lastStation)

    return jsonify({"Reservation": "Deleted Successfully"})

