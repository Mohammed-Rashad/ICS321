from flask import Blueprint, jsonify
from app.decorators import token_required, role_required
bp = Blueprint('reports', __name__, url_prefix='/reports')

@bp.route('/active_trains', methods=['GET'])#all users
@token_required
def active_trains():
    return jsonify({"message": "This is a sample active_trains report"})

@bp.route('/list_stations', methods=['GET'])#admins
@token_required
@role_required('admin')
def list_stations():
    return jsonify({"message": "This is a sample list_stations report"})

@bp.route('/reservation_details', methods=['GET'])#passenger
@token_required
@role_required('user')
def reservation_details():
    return jsonify({"message": "This is a sample reservation_details report"})

@bp.route('/waitlisted_passengers', methods=['GET'])#admins
@token_required
@role_required('admin')
def waitlisted_passengers():
    return jsonify({"message": "This is a sample waitlisted_passengers report"})

@bp.route('/average_load', methods=['GET'])#admins
@token_required
@role_required('admin')
def average_load():
    return jsonify({"message": "This is a sample average_load report"})

@bp.route('/list_dependents', methods=['GET'])#admins
@token_required
@role_required('admin')
def list_dependents():
    return jsonify({"message": "This is a sample list_dependents report"})
