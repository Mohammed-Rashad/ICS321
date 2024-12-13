from flask import Blueprint, jsonify, request
from app.decorators import token_required
bp = Blueprint('system', __name__, url_prefix= '/idk')

@bp.route('/notifications', methods = ['GET'])
@token_required
def send_notification():
    return jsonify()

@bp.route('/departure_message', methods = ['GET'])
@token_required
def departure_message():
    return jsonify()
