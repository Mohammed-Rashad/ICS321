from flask import Flask, render_template, session, make_response, request, jsonify
from flask_jwt_extended import JWTManager
import jwt
from datetime import datetime, timedelta
from functools import wraps

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
   
    # Initialize JWT
    JWTManager(app)

        
    def token_required(func):
        # decorator factory which invoks update_wrapper() method and passes decorated function as an argument
        @wraps(func)
        def decorated(*args, **kwargs):
            token = request.args.get('token')
            if not token:
                return jsonify({'Alert!': 'Token is missing!'}), 401

            try:

                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])

            # You can use the JWT errors in exception
            # except jwt.InvalidTokenError:
            #     return 'Invalid token. Please log in again.'
            except:
                return jsonify({'Message': 'Invalid token'}), 403
            return func(*args, **kwargs)
        return decorated

    # Register Blueprints
    from app.routes.auth import bp as auth_bp
    from app.routes.reports import bp as reports_bp
    from app.routes.passenger import bp as passenger_bp
    from app.routes.admin import bp as admin_bp
    from app.routes.system import bp as system_bp
    app.register_blueprint(system_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(passenger_bp)


    @app.route('/')
    def home():
        if not session.get('logged_in'):
            #add login page .html to parameter vvv
            return jsonify({"login page": "enter username & password"})
        else:
            return 'logged in currently'

    return app
