from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.Get import getPassenger, getReservation, getTrip
from Database.insert import insertWaitlist, insertReservation
from Constants import TICKET_PRICE as TP

# Create a blueprint for passenger-related routes
bp = Blueprint('passenger', __name__, url_prefix='/passenger')

@bp.route('/search_trains', methods=['GET'])
@token_required
@role_required('user')
def search_trains():

    ##placeholder BS
    # source = request.args.get('source')
    # destination = request.args.get('destination')
    # travel_date = request.args.get('date')
    
    # if not all([source, destination, travel_date]):
    #     return jsonify({"error": "Missing required parameters"}), 400

    # # Placeholder logic
    #return jsonify({"message": f"Searching trains from {source} to {destination} on {travel_date}"})

    return jsonify({"search":"placeholder"})

@bp.route('/book_seats', methods = ['POST'])
@token_required
@role_required('user')
def book_seats():
    data = request.json
    passengerID = data.get('passengerID')
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    firstStation = data.get('firstStation')
    lastStation = data.get('lastStation')

    passenger_information = getPassenger(passengerID)
    availablebalance = passenger_information.get('balance') 
    trip_data = getTrip(tripNumber, date)
    if trip_data.get(''):##CHECK SEATS      

        if availablebalance < TP:
            return jsonify({"Not enough funds in wallet":"Reservation Aborted"})
        else:
            ##update balance
            insertReservation(passengerID,tripNumber,date,firstStation,lastStation)
            return jsonify({"Seat":"Booked Successfully"})

    else:
        insertWaitlist(passengerID,tripNumber,date,firstStation,lastStation)
        return jsonify({"Seats Unavailable":"Waitlisted Successfully"})


    
@bp.route('/complete_payment', methods = ['GET'])
@token_required
@role_required('user')
def complete_payment():
    
    return jsonify({"Payment":"Successful"})
