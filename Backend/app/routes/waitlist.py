from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.insert import insertWaitlist
from Database.Delete import deleteWaitlist
from Database.Get import getWaitlist
bp = Blueprint('waitlist', __name__, url_prefix='/waitlist')

@bp.route('/insert_waitlist', methods=['POST'])
@token_required
@role_required('admin')
def insert_waitlist():
    data = request.json
    passengerID = data.get('passengerID')
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    firstStation = data.get('firstStation')
    lastStation = data.get('lastStation')
   
    insertWaitlist(passengerID, tripNumber, date, firstStation, lastStation)

    return jsonify({"Waitlist": "Inserted Successfully"})


@bp.route('/get_waitlist', methods=['GET'])
@token_required
@role_required('admin')
def get_waitlist():
    data = request.json
    passengerID = data.get('passengerID')
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    firstStation = data.get('firstStation')
    lastStation = data.get('lastStation')
   
    waitlist = getWaitlist(passengerID, tripNumber, date, firstStation, lastStation)

    return jsonify({"Waitlist": waitlist})


@bp.route('/delete_waitlist', methods=['POST'])
@token_required
@role_required('admin')
def delete_waitlist():
    data = request.json
    passengerID = data.get('passengerID')
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    firstStation = data.get('firstStation')
    lastStation = data.get('lastStation')
   
    deleteWaitlist(passengerID, tripNumber, date, firstStation, lastStation)

    return jsonify({"Waitlist": "Deleted Successfully"})

