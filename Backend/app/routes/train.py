from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.insert import insertTrain
from Database.Delete import deleteTrain
from Database.Get import getTrain
bp = Blueprint('train', __name__, url_prefix='/train')

@bp.route('/insert_train', methods=['POST'])


# @token_required
@role_required('admin')
def insert_train():
    data = request.json
    name = data.get('name')
    number = data.get('number')
    # list of stations
    stations = data.get('stations')
    # generate random 32bit number randomly 
    
    max_passengers = data.get('max_passengers')
    print("hi")
    insertTrain(number, max_passengers)

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
@token_required
@role_required('admin')
def delete_train():
    data = request.json
    number = data.get('number')

    deleteTrain(number)

    return jsonify({"Train": "Inserted Successfully"})


