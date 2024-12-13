from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.insert import insertTrip, insertTripStop
from Database.Delete import deleteTrip, deleteTripStop
from Database.Get import getTrip, getTripStop
bp = Blueprint('trip', __name__, url_prefix='/trip')

##insert get delete functions for trip
@bp.route('/insert_trip', methods=['POST'])
@token_required
@role_required('admin')
def insert_trip(): 
    data = request.json
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    trainNumber = data.get('trainNumber')
   
    insertTrip(tripNumber, date, trainNumber)

    return jsonify({"Trip": "Inserted Successfully"})


@bp.route('/get_trip', methods=['GET'])
@token_required
@role_required('admin')
def get_trip():
    data = request.json
    tripNumber = data.get('tripNumber')
    date = data.get('date')
   
    trip = getTrip(tripNumber, date)

    return jsonify({"Trip": trip})

@bp.route('/delete_trip', methods=['POST'])
@token_required
@role_required('admin')
def delete_trip():
    data = request.json
    tripNumber = data.get('tripNumber')
    date = data.get('date')
   
    deleteTrip(tripNumber, date)

    return jsonify({"Trip": "Deleted Successfully"})


##insert get delete functions for tripStop
@bp.route('/insert_tripStop', methods=['POST'])
@token_required
@role_required('admin')
def insert_tripStop():
    data = request.json
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    stopOrder = data.get('stopOrder')
    stationName = data.get('stationName')

    insertTripStop(tripNumber, date, stopOrder, stationName)

    return jsonify({"TripStop": "Inserted Successfully"})


@bp.route('/get_tripStop', methods=['GET'])
@token_required
@role_required('admin')
def get_tripStop():
    data = request.json
    tripNumber = data.get('tripNumber')
    date = data.get('date')
   
    tripStop = getTripStop(tripNumber, date)

    return jsonify({"TripStop": tripStop})

@bp.route('/delete_tripStop', methods=['POST'])
@token_required
@role_required('admin')
def delete_tripStop():
    data = request.json
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    stopOrder = data.get('stopOrder')
    deleteTripStop(tripNumber, date, stopOrder)

    return jsonify({"TripStop": "Deleted Successfully"})

