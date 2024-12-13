from flask import Blueprint, jsonify, request
from app.decorators import token_required

# Create a blueprint for passenger-related routes
bp = Blueprint('passenger', __name__, url_prefix='/passenger')

@bp.route('/search_trains', methods=['GET'])
@token_required
def search_trains():
    source = request.args.get('source')
    destination = request.args.get('destination')
    travel_date = request.args.get('date')
    
    if not all([source, destination, travel_date]):
        return jsonify({"error": "Missing required parameters"}), 400

    # Placeholder logic
    return jsonify({"message": f"Searching trains from {source} to {destination} on {travel_date}"})

@bp.route('/book_seats', methods = ['GET'])
@token_required
def book_seats():
    return jsonify()

@bp.route('/complete_payment', methods = ['GET'])
@token_required
def complete_payment():
    return jsonify()
