from flask import Blueprint, jsonify, request
from services import alert_service

bp = Blueprint("road_controller", __name__)

@bp.route("/damage", methods=["POST"])
def report_damage():
    location = request.json.get("location")
    severity = request.json.get("severity")
    
    # Send alert to collector office
    alert_service.send_road_damage_alert(location, severity)
    
    return jsonify({"status": "damage_alert_sent"})
