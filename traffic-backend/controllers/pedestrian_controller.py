from flask import Blueprint, jsonify, request
from services import ai_service, raspberry_service

bp = Blueprint("pedestrian_controller", __name__)

@bp.route("/update", methods=["POST"])
def pedestrian_update():
    count = request.json.get("count", 0)
    
    if count >= 15:
        # AI decides to stop traffic for safety
        raspberry_service.turn_signal_red()
    
    return jsonify({"status": "pedestrian_checked"})
