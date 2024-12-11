from flask import Blueprint, jsonify

bp = Blueprint('reports', __name__, url_prefix='/reports')

@bp.route('/active_trains', methods=['GET'])
def sample_report():
    return jsonify({"message": "This is a sample active_trains report"})
