from flask import Blueprint, jsonify, request
from services import ai_service, raspberry_service

bp = Blueprint("traffic_controller", __name__)

# Example: Adjust signal timings dynamically
@bp.route("/update_signal", methods=["POST"])
def update_signal():
    data = request.json
    traffic_density = data.get("density", 0)
    
    # AI service predicts optimal timing
    timings = ai_service.calculate_signal_timing(traffic_density)
    
    # Send to Raspberry Pi to update lights & 7-segment display
    raspberry_service.update_traffic_signal(timings)
    
    return jsonify({"status": "success", "timings": timings})
