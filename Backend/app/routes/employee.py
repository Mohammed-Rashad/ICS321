from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.insert import insertEmployee
from Database.Delete import deleteEmployee
from Database.Get import getEmployee
bp = Blueprint('employee', __name__, url_prefix='/employee')

@bp.route('/insert_employee', methods=['POST'])
@token_required
@role_required('admin')
def insert_employee():
    data = request.json
    id = data.get('id')
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')
    salary = data.get('salary')
   
    insertEmployee(id, email, password, name, salary)

    return jsonify({"Employee": "Inserted Successfully"})


@bp.route('/get_employee', methods=['GET'])
@token_required
@role_required('admin')
def get_employee():
    data = request.json
    id = data.get('id')
   
    employee = getEmployee(id)

    return jsonify({"Employee": employee})


@bp.route('/delete_employee', methods=['POST'])
@token_required
@role_required('admin')
def delete_employee():
    data = request.json
    id = data.get('id')
   
    deleteEmployee(id)

    return jsonify({"Employee": "Deleted Successfully"})

