from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.insert import insertTrain
from Database.Delete import deleteTrain
from Database.Get import getTrain, getAllTrains
bp = Blueprint('train', __name__, url_prefix='/train')

@bp.route('/insert_train', methods=['POST'])


# @token_required
def insert_train():
    data = request.json
    name = data.get('name')
    number = data.get('id')
    # list of stations
    stations = data.get('stations')
    # generate random 32bit number randomly 
    
    max_passengers = data.get('max_passengers')
    print("hi")    
    cost = data.get('cost')
    print(data)
    print(number, max_passengers,cost)
    insertTrain(number, max_passengers,cost)

    return jsonify({"Train": "Inserted Successfully"})


@bp.route('/get_train', methods=['GET'])
@token_required
@role_required('admin')
def get_train():
    data = request.json
    number = data.get('number')

    train = getTrain(number)

    return jsonify({"Train": train })


@bp.route('/delete_train', methods=['POST'])
@role_required('admin')
def delete_train():
    data = request.json
    number = data.get('number')

    deleteTrain(number)

    return jsonify({"Train": "Inserted Successfully"})

# get all trains
@bp.route('/all', methods=['GET'])
def all():
    trains = getAllTrains()
    if not trains:
        return jsonify({"Trains": []})
    trainsList = []
    for train in trains:
        print(train)
        trainNumber, maxPassengers, cost = train
        trainsList.append({"trainNumber": trainNumber, "maxPassengers": maxPassengers, "cost": cost})
        
    return jsonify({"Trains": trainsList}) 


