from flask import Blueprint, jsonify, request
from app.decorators import token_required

# Create a blueprint for passenger-related routes
bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/add_reservation', methods=['GET'])
@token_required
def add_reservation():
    return jsonify({"feedback":"this works"})

@bp.route('/edit_reservation', methods=['GET'])
@token_required
def edit_reservation():
    return jsonify({"feedback":"this works"})

@bp.route('/cancel_reservation', methods=['GET'])
@token_required
def cancel_reservation():
    return jsonify({"feedback":"this works"})


@bp.route('/assign_staff', methods=['POST'])
@token_required
def assign_staff():
    return jsonify({"feedback":"this works"})

@bp.route('/promote_passenger', methods=['GET'])
@token_required
def promote_passenger():
    return jsonify({"feedback":"this works"})