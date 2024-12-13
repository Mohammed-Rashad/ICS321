from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.insert import insertReservation
from Database.Get import getReservation
from Database.Delete import deleteReservation
from Database.Connect import connectToDatabase

# Create a blueprint for passenger-related routes
bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/add_reservation', methods=['POST'])
@token_required
@role_required
def add_reservation():

    data = request.json
    passengerID = data.get('passengerID')
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    firstStation = data.get('firstStation')
    lastStation = data.get('lastStation')
    seatNumber = data.get('seatNumber')

    insertReservation(passengerID, tripNumber, date, firstStation, lastStation, seatNumber)

   
    return jsonify({"Reservation":"Added Successfully"})


@bp.route('/edit_reservation', methods=['GET'])
@token_required
@role_required('admin')
def edit_reservation():
    ##garbage redo all, wait for update queries
    # data = request.json
    # passengerID = data.get('passengerID')
    # tripNumber = data.get('tripNumber')
    # date = data.get('date')
    # firstStation = data.get('firstStation')
    # lastStation = data.get('lastStation')
    # deleteReservation(passengerID, tripNumber, date, firstStation, lastStation)

    # data = request.json
    # passengerID = data.get('passengerID')
    # tripNumber = data.get('tripNumber')
    # date = data.get('date')
    # firstStation = data.get('firstStation')
    # lastStation = data.get('lastStation')
    # seatNumber = data.get('seatNumber')
    # insertReservation(passengerID, tripNumber, date, firstStation, lastStation, seatNumber)

    return jsonify({"feedback":"this works"})


@bp.route('/cancel_reservation', methods=['POST'])
@token_required
@role_required('admin')
def cancel_reservation():
    data = request.json
    passengerID = data.get('passengerID')
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    firstStation = data.get('firstStation')
    lastStation = data.get('lastStation')
   
    deleteReservation(passengerID, tripNumber, date, firstStation, lastStation)

    return jsonify({"Reservation":"Deleted Successfully"})


@bp.route('/assign_staff', methods=['POST'])
@token_required
@role_required('admin')
def assign_staff():
    return jsonify({"feedback":"this works"})


@bp.route('/promote_passenger', methods=['GET'])
@token_required
@role_required('admin')
def promote_passenger():
    return jsonify({"feedback":"this works"})