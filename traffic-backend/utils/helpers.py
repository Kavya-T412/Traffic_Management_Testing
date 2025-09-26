# utils/helpers.py
import RPi.GPIO as GPIO
import time
from config import SEGMENTS  # your mapping of segments to GPIO pins

# 7-segment digit mapping (common cathode)
SEGMENT_MAP = {
    0: ['A','B','C','D','E','F'],
    1: ['B','C'],
    2: ['A','B','G','E','D'],
    3: ['A','B','C','D','G'],
    4: ['F','G','B','C'],
    5: ['A','F','G','C','D'],
    6: ['A','F','G','E','C','D'],
    7: ['A','B','C'],
    8: ['A','B','C','D','E','F','G'],
    9: ['A','B','C','D','F','G']
}

def setup_gpio():
    """Setup GPIO pins for 7-segment display"""
    GPIO.setmode(GPIO.BCM)
    for pin in SEGMENTS.values():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

def clear_display():
    """Turn off all segments"""
    for pin in SEGMENTS.values():
        GPIO.output(pin, 0)

def digit_to_segments(digit):
    """Return the segments to light for a digit"""
    return SEGMENT_MAP.get(digit, [])

def display_digit(digit):
    """Display a single digit on the 7-segment display"""
    clear_display()
    for seg in digit_to_segments(digit):
        GPIO.output(SEGMENTS[seg], 1)

def display_number(number):
    """Display a 2-digit number (0-99)"""
    if number > 99:
        number = 99
    tens = number // 10
    ones = number % 10

    # Display tens
    display_digit(tens)
    time.sleep(0.5)  # half-second for tens
    clear_display()

    # Display ones
    display_digit(ones)
    time.sleep(0.5)
    clear_display()

def countdown_timer(seconds):
    """Show countdown on 7-segment display"""
    while seconds >= 0:
        display_number(seconds)
        seconds -= 1
