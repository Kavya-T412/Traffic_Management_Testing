import random

def calculate_signal_timing(density):
    # Simple AI placeholder: adaptive timing based on vehicle density
    base_time = 30
    red_time = base_time + int(density*0.5)
    green_time = base_time - int(density*0.2)
    yellow_time = 5
    return {"red": red_time, "yellow": yellow_time, "green": green_time}
