from flask import Flask
from flask_jwt_extended import JWTManager

from my_flask_app.app.routes import passenger

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize JWT
    JWTManager(app)

    # Register Blueprints
    from app.routes.auth import bp as auth_bp
    from app.routes.reports import bp as reports_bp
    from app.routes.passenger import bp as passenger_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(passenger_bp)

    return app
