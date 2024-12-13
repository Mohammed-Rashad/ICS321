from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
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