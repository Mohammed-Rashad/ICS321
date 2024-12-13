from flask import Blueprint, jsonify, request
from app.decorators import token_required
bp = Blueprint('system', __name__, url_prefix= '/idk')

@bp.route('/notifications', methods = ['GET'])
@token_required
def send_notification():
    data = request.json
    username = data.get('username')
    
    return jsonify({"Notification":"Has Been Sent"})


@bp.route('/departure_message', methods = ['GET'])
@token_required
def departure_message():
    return jsonify({"Alert":"Trip leaves in 3 Hours"})
