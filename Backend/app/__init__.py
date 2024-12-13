from flask import Flask, session, jsonify
from flask_jwt_extended import JWTManager
from Database.Connect import connectToDatabase
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    # Connect to database
    conn = connectToDatabase() #database connector
   
    # Initialize JWT
    JWTManager(app)
 

    # Register Blueprints
    ## normal routes
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

    ##other functions routes
    from app.routes.adminTools import bp as adminTools
    from app.routes.passengerTools import bp as passengerTools_bp
    from app.routes.train import bp as train_bp
    from app.routes.trip import bp as trip_bp
    app.register_blueprint(adminTools)
    app.register_blueprint(passengerTools_bp)
    app.register_blueprint(train_bp)
    app.register_blueprint(trip_bp)
    #not done yet...


    @app.route('/')
    def home():
        if not session.get('logged_in'):
            return jsonify({"login page": "enter username & password"})
        
        else:
            return 'logged in currently'

    return app
