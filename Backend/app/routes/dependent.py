from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.insert import insertDependent
from Database.Delete import deleteDependent
from Database.Get import getDependent
bp = Blueprint('dependent', __name__, url_prefix='/dependent')

@bp.route('/insert_dependent', methods=['POST'])
@token_required
@role_required('admin')
def insert_dependent():
    data = request.json
    id = data.get('id')
    name = data.get('name')
    guardianID = data.get('guardianID')
   
    insertDependent(id, name, guardianID)

    return jsonify({"Dependent": "Inserted Successfully"})


@bp.route('/get_dependent', methods=['GET'])
@token_required
@role_required('admin')
def get_dependent():
    data = request.json
    id = data.get('id')
   
    dependent = getDependent(id)

    return jsonify({"Dependent": dependent})


@bp.route('/delete_dependent', methods=['POST'])
@token_required
@role_required('admin')
def delete_dependent():
    data = request.json
    id = data.get('id')
   
    deleteDependent(id)

    return jsonify({"Dependent": "Deleted Successfully"})

