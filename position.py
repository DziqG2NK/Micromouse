from machine import Pin, time_pulse_us
import time

TRIG_FRONT = Pin(6, Pin.OUT)
TRIG_LEFT = Pin(7, Pin.OUT)
TRIG_RIGHT = Pin(8, Pin.OUT)

ECHO_FRONT = Pin(2, Pin.IN)
ECHO_LEFT = Pin(3, Pin.IN)
ECHO_RIGHT = Pin(4, Pin.IN)


elems = [(TRIG_FRONT, ECHO_FRONT), (TRIG_LEFT, ECHO_LEFT), (TRIG_RIGHT, ECHO_RIGHT)]

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

while True:
    measurements = [None, None, None]
    for i, (trigger, echo) in enumerate(elems):
        measurements[i] = measure_distance(trigger, echo)
    
    if measurements[0] is not None and measurements[1] is not None:
        print("Odległość przedniego: {:.2f} cm".format(measurements[0]))
        print("Odległość lewego: {:.2f} cm".format(measurements[1]))
        print("Odległość prawego: {:.2f} cm".format(measurements[2]))
    else:
        print("Brak echa")
    time.sleep(0.5)