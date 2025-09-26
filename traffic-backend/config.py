# config.py

# Twilio configuration for alerts
TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE_NUMBER = "+1234567890"
COLLECTOR_PHONE_NUMBER = "+9876543210"

# MQTT broker configuration for Raspberry Pi communication
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883

# AI Model Paths
YOLO_MODEL_PATH = "models/yolov8_traffic.pt"
ACCIDENT_MODEL_PATH = "models/yolov8_accident.pt"

# GPIO pins for Raspberry Pi traffic light
RED_PIN = 17
YELLOW_PIN = 27
GREEN_PIN = 22

# GPIO pins for 7-segment display (common cathode)
SEGMENTS = {'A':5,'B':6,'C':13,'D':19,'E':26,'F':12,'G':16,'DP':20}
