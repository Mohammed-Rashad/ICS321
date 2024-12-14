from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
# from Database.Get import getPassenger, getReservation, getTripStop, getPassengerByEmail
# from Database.insert import insertWaitlist, insertReservation, insertPassenger
# from Database.ProcessFunctionality import searchForTrain, availableSeats, canAfford, pay, getAllReservations
from Database import Get as getDb
from Database import insert as insertDb
from Database import ProcessFunctionality as processDb
# from Database import Constants as Constants
from Database import Delete as deleteDb
# from Constants import TICKET_PRICE as TP
TP = 47
# Create a blueprint for passenger-related routes
bp = Blueprint('passenger', __name__, url_prefix='/passenger')

@bp.route('/search_trains', methods=['GET'])
@token_required
@role_required('user')
def search_trains():
    data = request.json
    initialStation = data.get('initialStation')
    finalStation = data.get('finalStation')
    date = data.get('date')

    available_trains = getDb.searchForTrain(initialStation, finalStation, date)

    return jsonify({"Available Trains":available_trains})
# @bp.route('/book_seats', methods = ['POST'])
# def book_seats():

# @bp.route('/book_seats', methods = ['POST'])
# def book_seats():
#     data = request.json
#     #passengerID is a list of passenger and dependent ids who want to book the train with the passenger at index 0 
#     passengerIDs = data.get('passengerIDs')
#     tripNumber = data.get('tripNumber')
#     date = data.get('date')
#     stopOrder = data.get('stopOrder')

#     trip_data = getTripStop(tripNumber, date, stopOrder)#get the initial and final stations from the tripNumber

#     firstStation = trip_data.get('firstStation')
#     lastStation = trip_data.get('lastStation')

#     seatList = availableSeats(tripNumber, date, firstStation, lastStation)

#     if len(seatList) >= len(passengerIDs):##CHECK SEATS are enough     

#         if canAfford(passengerIDs):#check if all passenger can afford
#             seatIterator = 0

#             for id in passengerIDs: #create reservation for each
#                 seatNumber = seatList[seatIterator]
#                 insertReservation(id,tripNumber,date,firstStation,lastStation, seatNumber)
#                 seatIterator +=1

#             return jsonify({"Seat/s":"Booked Successfully"})
            
#         else:
#             return jsonify({"Balance Not Enough":"Reservation Aborted"})

#     else:
#         for id in passengerIDs: #create waitlist for each
#                 insertWaitlist(id,tripNumber,date,firstStation,lastStation) 

#         return jsonify({"Seats Unavailable":"Waitlisted Successfully"})


    
@bp.route('/complete_payment', methods = ['GET'])
# @token_required
@role_required('user')
def complete_payment():
    data = request.json
    passengerID = data.get('passengerID')
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    stopOrder = data.get('stopOrder')

    trip_data = getDb.getTripStop(tripNumber, date, stopOrder)#get the initial and final stations from the tripNumber

    firstStation = trip_data.get('firstStation')
    lastStation = trip_data.get('lastStation')
    if pay(passengerID, tripNumber, date, firstStation, lastStation):
        tickets = {}  # Initialize an empty dictionary to hold all tickets

        # Iterate over all reservations for the passenger
        for each in getDb.getAllReservations(passengerID):
            tripNumber = each.get('TripNumber')  # Get the trip number from the reservation
            seatNumber = each.get('SeatNumber')  # Get the seat number from the reservation
            tickets[tripNumber] = seatNumber  # Add the trip number and seat number to the dictionary

        # Return the dictionary of tickets as part of the response
        return jsonify({"Payment Successful": tickets})

    else:
        return jsonify({"Payment Unsuccessful":"Payment Incompleted"})
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
        getDb.insertPassenger(name, 0,  password, email, phone)
        return jsonify({"message": "Passenger created successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500
        

