from flask import Flask, jsonify, request
from flask_cors import CORS

from controllers import traffic_controller, accident_controller, pedestrian_controller, road_controller

app = Flask(__name__)
CORS(app)

# Traffic routes
app.register_blueprint(traffic_controller.bp, url_prefix="/traffic")
app.register_blueprint(accident_controller.bp, url_prefix="/accident")
app.register_blueprint(pedestrian_controller.bp, url_prefix="/pedestrian")
app.register_blueprint(road_controller.bp, url_prefix="/road")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
