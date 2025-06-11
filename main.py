from machine import Pin, time_pulse_us
from motors import some_fun
import time

trigger_1 = Pin(3, Pin.OUT)
echo_1 = Pin(2, Pin.IN)

trigger_2 = Pin(7, Pin.OUT)
echo_2 = Pin(6, Pin.IN)

trigger_3 = Pin(7, Pin.OUT)
echo_3 = Pin(6, Pin.IN)

elems = [(trigger_1, echo_1), (trigger_2, echo_2)]

def measure_distance(trigger, echo):

    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(10)
    trigger.low()

    # Measure echo pulse width
    duration = time_pulse_us(echo, 1, 30000)  # 30 ms timeout
    if duration < 0:
        return None  # timeout

    distance_cm = duration / 58.0  # według dokumentacji SRF05
    return distance_cm

some_fun()

"""
while True:
    measurements = [None, None]
    for i, (trigger, echo) in enumerate(elems):
        measurements[i] = measure_distance(trigger, echo)
    
    if measurements[0] is not None and measurements[1] is not None:
        print("Odległość pierwszego: {:.2f} cm".format(measurements[0]))
        print("Odległość drugiego: {:.2f} cm".format(measurements[1]))
    else:
        print("Brak echa")
    time.sleep(0.5)
"""