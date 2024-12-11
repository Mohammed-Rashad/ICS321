from flask import Blueprint, jsonify, request

bp = Blueprint('system', __name__, url_prefix= '')

@bp.route('/notifications', methods = ['GET'])
def send_notification():
    return jsonify()

@bp.route('/departure_message', methods = ['GET'])
def departure_message():
    return jsonify()
