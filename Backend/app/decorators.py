from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from flask import session, jsonify
from functools import wraps

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        try:
            verify_jwt_in_request()  # This automatically checks the token validity
            user_identity = get_jwt_identity()  # Optionally fetch the identity from the token
        except Exception as e:
            return {"message": str(e)}, 401
        return func(*args, **kwargs)
    return decorated

def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not session.get('logged_in') or session.get('role') != role:
                return jsonify({"error": "Access denied"}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator
