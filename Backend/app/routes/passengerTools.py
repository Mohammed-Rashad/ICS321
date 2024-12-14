from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.insert import insertPassenger
from Database.Delete import deletePassenger
from Database.Get import getPassenger
bp = Blueprint('passengerTools', __name__, url_prefix='/passengerTools')

@bp.route('/insert_passenger', methods=['POST'])
@token_required
@role_required('admin')
def insert_passenger():
    data = request.json
    id = data.get('id')
    name = data.get('name')
    balance = data.get('balance')
    password = data.get('password')
    email = data.get('email')
    phone = data.get('phone')

    insertPassenger(id, name, balance, password, email, phone)

    return jsonify({"Passenger": "Inserted Successfully"})


@bp.route('/get_passenger', methods=['GET'])
@token_required
@role_required('admin')
def get_passenger():
    data = request.json
    id = data.get('id')

    passenger = getPassenger(id)

    return jsonify({"Passenger": passenger})

@bp.route('/delete_passenger', methods=['POST'])
@token_required
@role_required('admin')
def delete_passenger():
    data = request.json
  
    deletePassenger(id)

    return jsonify({"Passenger": "Deleted Successfully"})

