from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.insert import insertReservation
from Database.Connect import connectToDatabase

# Create a blueprint for passenger-related routes
bp = Blueprint('admin', __name__, url_prefix='/admin')
conn = connectToDatabase()

@bp.route('/add_reservation', methods=['POST'])
@token_required
@role_required
def add_reservation():
    try:
        conn = connectToDatabase
        data = request.json
        passengerID = data.get('passengerID')
        tripNumber = data.get('tripNumber')
        date = data.get('date')
        firstStation = data.get('firstStation')
        lastStation = data.get('lastStation')
        seatNumber = data.get('seatNumber')
        
        insertReservation(conn, passengerID, tripNumber, date, firstStation, lastStation, seatNumber)

    except Exception as e:
        return jsonify({"ERROR":"Invalid Input"})
    
    return jsonify({"Reservation":"Added Successfully"})

@bp.route('/edit_reservation', methods=['GET'])
@token_required
@role_required('admin')
def edit_reservation():
    return jsonify({"feedback":"this works"})

@bp.route('/cancel_reservation', methods=['GET'])
@token_required
@role_required('admin')
def cancel_reservation():
    return jsonify({"feedback":"this works"})


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