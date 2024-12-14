from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.insert import insertStation
from Database.Delete import deleteStation
from Database.Get import getStation
bp = Blueprint('station', __name__, url_prefix='/station')

@bp.route('/insert_station', methods=['POST'])
@token_required
@role_required('admin')
def insert_station():
    data = request.json
    name = data.get('name')
    city = data.get('city')
   
    insertStation(name, city)

    return jsonify({"Station": "Inserted Successfully"})


@bp.route('/get_station', methods=['GET'])
@token_required
@role_required('admin')
def get_station():
    data = request.json
    name = data.get('name')

    station = getStation(name)

    return jsonify({"Station": station})


@bp.route('/delete_station', methods=['POST'])
@token_required
@role_required('admin')
def delete_station():
    data = request.json
    name = data.get('name')
  
    deleteStation(name)

    return jsonify({"Station": "Deleted Successfully"})

