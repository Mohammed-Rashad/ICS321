from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.insert import insertReservation, insertAssigned
from Database.Delete import deleteReservation, deleteWaitlist
from Database.Get import getPassenger
from Database.ProcessFunctionality import getAllWaitlists, getAllReservations, availableSeats

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
    data = request.json
    passengerID = data.get('passengerID')
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    firstStation = data.get('firstStation')
    lastStation = data.get('lastStation')

    if getPassenger(passengerID).get('HasPaid') == False:
        seatList = availableSeats(tripNumber, date, firstStation, lastStation)
        seatIterator = 0

        for each in getAllReservations:
            deleteReservation(passengerID, tripNumber, date, firstStation, lastStation)
            insertReservation(passengerID, tripNumber, date, firstStation, lastStation,seatList[seatIterator])
            
            seatIterator+=1
        return jsonify({"feedback":"this works"})
    
    else:
        return jsonify({"Passenger Paid Already":"Cannot Process Modification"})


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
    data = request.json
    employeeID = data.get('id')
    date = data.get('date') 
    trainNumber = data.get('trainNumber')

    insertAssigned(employeeID, date, trainNumber)

    return jsonify({"Employee":"Assigned  Succesfully"})


@bp.route('/promote_passenger', methods=['GET'])
@token_required
@role_required('admin')
def promote_passenger():
    data = request.json
    passengerID = data.get('id')

    seatIterator = 0
    for each in getAllWaitlists(passengerID):
        passengerID = each.get('PassengerID')
        tripNumber = each.get('TripNumber')
        date = each.get('Date')
        firstStation = each.get('FirstStation')
        lastStation = each.get('LastStation')

        seatList = availableSeats(tripNumber, date, firstStation, lastStation)
        seatNumber = seatList[seatIterator]

        deleteWaitlist(passengerID, tripNumber, date, firstStation, lastStation)
        insertReservation(passengerID, tripNumber, date, firstStation, lastStation, seatNumber)
        seatIterator +=1

    return jsonify({"Passenger/s":"Promoted Successfully"})