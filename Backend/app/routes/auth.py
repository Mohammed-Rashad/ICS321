from flask import Blueprint, request, jsonify, session
from flask_jwt_extended import create_access_token

bp = Blueprint('auth', __name__, url_prefix='/auth')

##replaced with userLogin
# @bp.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     username = data.get('username')
#     password = data.get('password')

#     # Replace with DB lookup
#     if username == "test" and password == "password":
#         session['logged_in'] = True

#         access_token = create_access_token(identity = username)
#         return jsonify(access_token=access_token), 200
#     else:
#         return jsonify({"error": "Invalid credentials"}), 401
    

@bp.route('/userLogout', methods = ['POST'])
def logout():
    session['logged_in'] = False
    return jsonify({"Logout":"successful"})

from Database import insert as db
from Database import Get as getDb

@bp.route('/adminLogin', methods=['POST'])
def adminLogin():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    result = getDb.checkAdmin(username, password) 
    if result:
        id, email, password = result
        # Create a session for the admin
        session['logged_in'] = True
        session['role'] = 'admin'
        session['username'] = id

        # Generate JWT
        access_token = create_access_token(identity={"username": username, "role": "admin"})
        print(session.get('logged_in'))
        print(session.get('role'))
        print(access_token)
        return jsonify({"role":"admin", "loggedIn":True}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
    

@bp.route('/userLogin', methods=['POST'])
def userLogin():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    print(email, password)
    result = getDb.checkUser(email, password)
    print(result)
    if result:
        id, email, password, name = result
        # Create a session for the normal user
        session['logged_in'] = True
        session['role'] = 'user'
        session['username'] = id

        # Generate JWT
        access_token = create_access_token(identity={"username": email, "role": "user"})
        
        return jsonify({"role":"user", "loggedIn":True, "username":name}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@bp.route('/adminlogout', methods = ['POST'])
def adminLogout():
    session['logged_in'] = False
    return jsonify({"Logout":"successful"})