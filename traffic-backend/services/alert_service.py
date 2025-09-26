from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, COLLECTOR_PHONE_NUMBER

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_accident_alert(location):
    message = f"Accident detected at {location}. Immediate action required!"
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=COLLECTOR_PHONE_NUMBER
    )

def send_road_damage_alert(location, severity):
    message = f"Road damage reported at {location} with severity {severity}."
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=COLLECTOR_PHONE_NUMBER
    )
