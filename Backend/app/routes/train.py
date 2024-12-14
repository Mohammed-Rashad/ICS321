from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.insert import insertTrain
from Database.Delete import deleteTrain
from Database.Get import getTrain
bp = Blueprint('train', __name__, url_prefix='/train')

@bp.route('/insert_train', methods=['POST'])
@token_required
@role_required('admin')
def insert_train():
    data = request.json
    number = data.get('number')
    max_passengers = data.get('max_passengers')
    cost = data.get('cost')

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
@token_required
@role_required('admin')
def delete_train():
    data = request.json
    number = data.get('number')

    deleteTrain(number)

    return jsonify({"Train": "Inserted Successfully"})


