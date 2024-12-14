from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.Get import getPassenger, getReservation, getTrip
from Database.insert import insertWaitlist, insertReservation
# from Constants import TICKET_PRICE as TP
from Database import Get as getDb
from Database import insert as Insertdb
from flask import session
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
    passengerID = session.get('username')
    print(passengerID)
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    firstStation = data.get('firstStation')
    lastStation = data.get('lastStation')
    
    passenger_information = getPassenger(passengerID)
    availablebalance = passenger_information.get('balance') 
    trip_data = getTrip(tripNumber, date)
    if trip_data.get(''):##CHECK SEATS      

        if availablebalance < 60:
            return jsonify({"Not enough funds in wallet":"Reservation Aborted"})
        else:
            ##update balance
            insertReservation(passengerID,tripNumber,date,firstStation,lastStation)
            return jsonify({"Seat":"Booked Successfully"})

    else:
        insertWaitlist(passengerID,tripNumber,date,firstStation,lastStation)
        return jsonify({"Seats Unavailable":"Waitlisted Successfully"})


    
@bp.route('/complete_payment', methods = ['GET'])
# @token_required
@role_required('user')
def complete_payment():
    return jsonify({"Payment":"Successful"})

# sign up route
# CREATE TABLE `passenger` (
#   `ID` int NOT NULL,
#   `Name` varchar(30) NOT NULL,
#   `Balance` int NOT NULL,
#   `password` varchar(255) NOT NULL,
#   `email` varchar(50) NOT NULL,
#   `phone` varchar(14) NOT NULL,
#   PRIMARY KEY (`ID`)
# )
@bp.route('/signup', methods = ['POST'])
def sign_up():
    try: 
        data = request.json
        email = data.get('email')
        id = data.get('id')
        password = data.get('password')
        name = data.get('name')
        phone = data.get('phone')
        # check if all required fields are present
        if not all([email, password, name, id]):
            return jsonify({"error": "Missing required fields"}), 400
        # check if passengerID already exists
        passenger = getDb.getPassenger(id)
        #  check emails are not the same
        if passenger:
            return jsonify({"error": "Passenger already exists"}), 400
        
        # check email is not used
        passengerWithEmail = getDb.getPassengerByEmail(email)
        if passengerWithEmail:
            return jsonify({"error": "Email already exists"}), 400

        # insert passenger into database
        Insertdb.insertPassenger(name, 0,  password, email, phone)
        return jsonify({"message": "Passenger created successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500
        

