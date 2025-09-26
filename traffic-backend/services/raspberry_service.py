import RPi.GPIO as GPIO
import time
from config import RED_PIN, YELLOW_PIN, GREEN_PIN, SEGMENTS

GPIO.setmode(GPIO.BCM)
GPIO.setup([RED_PIN, YELLOW_PIN, GREEN_PIN], GPIO.OUT)

for seg in SEGMENTS.values():
    GPIO.setup(seg, GPIO.OUT)
    GPIO.output(seg, 0)

def update_traffic_signal(timings):
    # Example: Red light
    GPIO.output(RED_PIN, 1)
    display_time(timings['red'])
    time.sleep(timings['red'])
    
    # Yellow light
    GPIO.output(RED_PIN, 0)
    GPIO.output(YELLOW_PIN, 1)
    display_time(timings['yellow'])
    time.sleep(timings['yellow'])
    
    # Green light
    GPIO.output(YELLOW_PIN, 0)
    GPIO.output(GREEN_PIN, 1)
    display_time(timings['green'])
    time.sleep(timings['green'])
    
    GPIO.output(GREEN_PIN, 0)

def turn_signal_red():
    GPIO.output(RED_PIN, 1)
    GPIO.output(YELLOW_PIN, 0)
    GPIO.output(GREEN_PIN, 0)

def display_time(seconds):
    # Simple 7-segment placeholder: implement digit display
    print(f"Displaying {seconds} seconds on 7-segment")




from helpers import setup_gpio, countdown_timer
import time

setup_gpio()

# Example: Green light for 10 seconds
print("Green Light ON")
# turn on green GPIO pin here
countdown_timer(10)
# turn off green GPIO pin here

# Example: Yellow light for 3 seconds
print("Yellow Light ON")
# turn on yellow GPIO pin here
countdown_timer(3)
# turn off yellow GPIO pin here

# Example: Red light for 7 seconds
print("Red Light ON")
# turn on red GPIO pin here
countdown_timer(7)
# turn off red GPIO pin here
