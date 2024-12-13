from flask import Flask, session, jsonify
from flask_jwt_extended import JWTManager
from Database.Connect import connectToDatabase
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    CORS(app)
    # Connect to database
    conn = connectToDatabase() #database connector
   
    # Initialize JWT
    JWTManager(app)


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
            return jsonify({"login page": "enter username & password"})
        
        else:
            return 'logged in currently'

    return app
