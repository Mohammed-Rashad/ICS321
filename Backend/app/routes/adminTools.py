from flask import Blueprint, jsonify, request
from app.decorators import token_required, role_required
from Database.insert import insertAdmin
from Database.Delete import deleteAdmin
from Database.Get import getAdmin
bp = Blueprint('adminTools', __name__, url_prefix='/adminTools')

@bp.route('/insert_admin', methods=['POST'])
@token_required
@role_required('admin')
def insert_admin():
    data = request.json
    id = data.get('id')
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')
    salary = data.get('salary')
   
    insertAdmin(id, email, password, name, salary)

    return jsonify({"Admin": "Inserted Successfully"})


@bp.route('/get_admin', methods=['GET'])
@token_required
@role_required('admin')
def get_admin():
    data = request.json
    id = data.get('id')

    admin = getAdmin(id)

    return jsonify({"Admin": admin})

@bp.route('/delete_admin', methods=['POST'])
@token_required
@role_required('admin')
def delete_admin():
    data = request.json
  
    deleteAdmin(id)

    return jsonify({"Admin": "Inserted Successfully"})

