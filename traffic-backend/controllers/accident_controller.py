from flask import Blueprint, jsonify, request
from services import alert_service

bp = Blueprint("accident_controller", __name__)

@bp.route("/report", methods=["POST"])
def report_accident():
    data = request.json
    location = data.get("location")
    
    # Send alert to ambulance & police
    alert_service.send_accident_alert(location)
    
    return jsonify({"status": "alert_sent"})
