from flask import Blueprint, request, jsonify, session
from flask_jwt_extended import create_access_token

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Replace with DB lookup
    if username == "test" and password == "password":
        session['logged_in'] = True

        access_token = create_access_token(identity = username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
    

@bp.route('/logout', methods = ['POST'])
def logout():
    session['logged_in'] = False
    return jsonify({"Logout":"succesful"})