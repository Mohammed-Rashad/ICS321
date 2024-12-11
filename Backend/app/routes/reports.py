from flask import Blueprint, jsonify

bp = Blueprint('reports', __name__, url_prefix='/reports')

@bp.route('/active_trains', methods=['GET'])
def active_trains():
    return jsonify({"message": "This is a sample active_trains report"})

@bp.route('/list_stations', methods=['GET'])
def list_stations():
    return jsonify({"message": "This is a sample list_stations report"})

@bp.route('/reservation_details', methods=['GET'])
def reservation_details():
    return jsonify({"message": "This is a sample reservation_details report"})

@bp.route('/waitlisted_passengers', methods=['GET'])
def waitlisted_passengers():
    return jsonify({"message": "This is a sample waitlisted_passengers report"})

@bp.route('/average_load', methods=['GET'])
def average_load():
    return jsonify({"message": "This is a sample average_load report"})

@bp.route('/list_dependents', methods=['GET'])
def list_dependents():
    return jsonify({"message": "This is a sample list_dependents report"})
