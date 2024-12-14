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
@bp.route('/book', methods=['GET'])
def bookTrip():
    try:
        data = request.json
        print(data)
        passengerId = data.get("passengerId")
        tripNumber = data.get("tripNumber")
        date = data.get("date")
        tripDetails = getDb.getAllTrainStopsForTrip(tripNumber, date)
        # print(tripDetails)
        initialStation = tripDetails[0][2]
        finalStation = tripDetails[-1][2]
        print("################################################################")

        available_seats = pfDb.availableSeats(tripNumber, date, initialStation, finalStation)
        if len(available_seats) == 0:
            pass
        else:
            seat = available_seats[0]
            
            db.insertReservation(passengerId, tripNumber, date, tripDetails[0][3], tripDetails[-1][3], seat)
            return jsonify({"message": "Done"}), 200
    except:
        return jsonify({"error": "something wrong"}), 404