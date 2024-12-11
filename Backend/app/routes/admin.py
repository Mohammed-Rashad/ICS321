from flask import Blueprint, jsonify, request

# Create a blueprint for passenger-related routes
bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/add_reservation', methods=['GET'])
def add_reservation():
    return jsonify()

@bp.route('/edit_reservation', methods=['GET'])
def edit_reservation():
    return jsonify()

@bp.route('/cancel_reservation', methods=['GET'])
def cancel_reservation():
    return jsonify()


@bp.route('/assign_staff', methods=['POST'])
def assign_staff():
    return jsonify()

@bp.route('/promote_passenger', methods=['GET'])
def promote_passenger():
    return jsonify()