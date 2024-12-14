from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.Get import getPassenger, getReservation, getTripStop
from Database.insert import insertWaitlist, insertReservation
from Database.ProcessFunctionality import searchForTrain, availableSeats, canAfford, pay, getAllReservations
from Constants import TICKET_PRICE as TP

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

    available_trains = searchForTrain(initialStation, finalStation, date)

    return jsonify({"Available Trains":available_trains})

@bp.route('/book_seats', methods = ['POST'])
@token_required
@role_required('user')
def book_seats():
    data = request.json
    #passengerID is a list of passenger and dependent ids who want to book the train with the passenger at index 0 
    passengerIDs = data.get('passengerIDs')
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    stopOrder = data.get('stopOrder')

    trip_data = getTripStop(tripNumber, date, stopOrder)#get the initial and final stations from the tripNumber

    firstStation = trip_data.get('firstStation')
    lastStation = trip_data.get('lastStation')

    seatList = availableSeats(tripNumber, date, firstStation, lastStation)

    if len(seatList) >= len(passengerIDs):##CHECK SEATS are enough     

        if canAfford(passengerIDs):#check if all passenger can afford
            seatIterator = 0

            for id in passengerIDs: #create reservation for each
                seatNumber = seatList[seatIterator]
                insertReservation(id,tripNumber,date,firstStation,lastStation, seatNumber)
                seatIterator +=1

            return jsonify({"Seat/s":"Booked Successfully"})
            
        else:
            return jsonify({"Balance Not Enough":"Reservation Aborted"})

    else:
        for id in passengerIDs: #create waitlist for each
                insertWaitlist(id,tripNumber,date,firstStation,lastStation) 

        return jsonify({"Seats Unavailable":"Waitlisted Successfully"})


    
@bp.route('/complete_payment', methods = ['GET'])
@token_required
@role_required('user')
def complete_payment():
    data = request.json
    passengerID = data.get('passengerID')
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    stopOrder = data.get('stopOrder')

    trip_data = getTripStop(tripNumber, date, stopOrder)#get the initial and final stations from the tripNumber

    firstStation = trip_data.get('firstStation')
    lastStation = trip_data.get('lastStation')
    if pay(passengerID, tripNumber, date, firstStation, lastStation):
        tickets = {}  # Initialize an empty dictionary to hold all tickets

        # Iterate over all reservations for the passenger
        for each in getAllReservations(passengerID):
            tripNumber = each.get('TripNumber')  # Get the trip number from the reservation
            seatNumber = each.get('SeatNumber')  # Get the seat number from the reservation
            tickets[tripNumber] = seatNumber  # Add the trip number and seat number to the dictionary

        # Return the dictionary of tickets as part of the response
        return jsonify({"Payment Successful": tickets})

    else:
        return jsonify({"Payment Unsuccessful":"Payment Incompleted"})