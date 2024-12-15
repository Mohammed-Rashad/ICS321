from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database import insert as db
from Database import Get as getDb
from Database import Delete as deleteDb
from Database import ProcessFunctionality as pfDb
# from Database.insert import insertTrip, insertTripStop
# from Database.Delete import deleteTrip, deleteTripStop
# from Database.Get import getTrip, getTripStop
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
   
    db.insertTrip(tripNumber, date, trainNumber)

    return jsonify({"Trip": "Inserted Successfully"})


@bp.route('/get_trip', methods=['GET'])
@token_required
@role_required('admin')
def get_trip():
    data = request.json
    tripNumber = data.get('tripNumber')
    date = data.get('date')
   
    trip = getDb.getTrip(tripNumber, date)

    return jsonify({"Trip": trip})

@bp.route('/delete_trip', methods=['POST'])
@token_required
@role_required('admin')
def delete_trip():
    data = request.json
    tripNumber = data.get('tripNumber')
    date = data.get('date')
   
    deleteDb.deleteTrip(tripNumber, date)

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

    db.insertTripStop(tripNumber, date, stopOrder, stationName)

    return jsonify({"TripStop": "Inserted Successfully"})


@bp.route('/get_tripStop', methods=['GET'])
@token_required
@role_required('admin')
def get_tripStop():
    data = request.json
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    stopOrder = data.get('stopOrder')
    
    tripStop = getDb.getTripStop(tripNumber, date, stopOrder)

    return jsonify({"TripStop": tripStop})

@bp.route('/delete_tripStop', methods=['POST'])
@token_required
@role_required('admin')
def delete_tripStop():
    data = request.json
    tripNumber = data.get('tripNumber')
    date = data.get('date')
    stopOrder = data.get('stopOrder')
    deleteDb.deleteTripStop(tripNumber, date, stopOrder)

    return jsonify({"TripStop": "Deleted Successfully"})

from datetime import datetime, timedelta
# get all trips
@bp.route('/allFuture', methods=['GET'])
def getComingTrips():
    # current date
    datenow = datetime.now().date()
    time = datetime.now().time()
    # time_in_seconds = time.hour * 3600 + time.minute * 60 + time.second
    # time_as_timedelta = timedelta(seconds=time_in_seconds)
    # time = time_as_timedelta
    trips = getDb.getAllTrips(datenow)
    if not trips:
        return jsonify({"Trips": []})
    tripsList = []
    # print(trips)
    for trip in trips.values():
        tripNumber = trip["tripNumber"]
        trainNumber = trip["trainNumber"]
        date = trip["date"]
        stations = trip["stations"]
        times = trip["times"]
        times = [(datetime.min + value).time() for value in times]
        print(times)
        print("________________")
        if times[0] < time:
            continue
        times = [str(value) for value in times]
        tripsList.append({"tripNumber": tripNumber, "trainNumber": trainNumber, "date": date, "stations": stations, "times": times})
    
    print(tripsList)
        
    return jsonify({"Trips": tripsList})


# BOOK TRIP
# @bp.route('/book', methods=['GET'])
# def bookTrip():
#     try:
#         data = request.json
#         print(data)
#         passengerId = data.get("passengerId")
#         tripNumber = data.get("tripNumber")
#         date = data.get("date")
#         tripDetails = getDb.getAllTrainStopsForTrip(tripNumber, date)
#         # print(tripDetails)
#         initialStation = tripDetails[0][2]
#         finalStation = tripDetails[-1][2]
#         print("################################################################")

#         available_seats = pfDb.availableSeats(tripNumber, date, initialStation, finalStation)
#         if len(available_seats) == 0:
#             pass
#         else:
#             seat = available_seats[0]
            
#             db.insertBooking(passengerId, tripNumber, date, seat)
#             return jsonify({"message": "Done"}), 200
#     except:
#         return jsonify({"error": "something wrong"}), 404



@bp.route('/book', methods=['POST'])
def bookTrip():
    try:
        # Parse request data
        data = request.json
        passengerId = data.get("passengerId")
        tripNumber = data.get("tripNumber")
        date = data.get("date")
        # convert date text to delta
        date = datetime.strptime(date, '%d-%m-%Y').date()
        # assure all exist
        if not passengerId or not tripNumber or not date:
            return jsonify({"error": "Missing data"}), 400  # Bad request
        print(data)
        print("222222222222222222222222222222")
        # Retrieve trip details
        tripDetails = getDb.getAllTrainStopsForTrip(tripNumber, date)
        initialStation = tripDetails[0][2]
        finalStation = tripDetails[-1][2]
        print("################################################################")

        # Check available seats
        available_seats = pfDb.availableSeats(tripNumber, date, initialStation, finalStation)
        if len(available_seats) == 0:
            return jsonify({"status": "waitlisted"}), 200  # No available seats (client error)
        else:
            seat = available_seats[0]
            
            # Insert booking
            db.insertBooking(passengerId, tripNumber, date, seat)
            return jsonify({"status": "reserved"}), 200
    
    except KeyError as e:  # Catch missing key error in request data
        print(f"Missing data: {str(e)}")  # Log the error
        return jsonify({"error": f"Missing data: {str(e)}"}), 400  # Bad request
    
    except Exception as e:  # Catch other unexpected errors
        print(f"Unexpected error: {str(e)}")  # Log the error
        return jsonify({"error": "Something went wrong"}), 500  # Internal server error

# pay
@bp.route('/pay', methods=['POST'])
def pay():
    try:
        # Parse request data
        data = request.json
        passengerId = data.get("passengerId")
        tripNumber = data.get("tripNumber")
        date = data.get("date")
        print(data)
        # convert date text to delta
        date = datetime.strptime(date, '%d-%m-%Y').date()
        print(date)
        # assure all exist
        if not passengerId or not tripNumber or not date:
            return jsonify({"error": "Missing data"}), 400  # Bad request
        isConfirmed = pfDb.confirmPayment(passengerId, tripNumber, date)
        if isConfirmed:
            return jsonify({"status": "confirmed"}), 200
        else:
            return jsonify({"status": "not confirmed"}), 400
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "something wrong"}), 404