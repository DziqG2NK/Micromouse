from machine import Pin, time_pulse_us
import time

trigger = Pin(11, Pin.OUT)
echo = Pin(8, Pin.IN)

def measure_distance():

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
    dist = measure_distance()
    if dist is not None:
        print("Odległość: {:.2f} cm".format(dist))
    else:
        print("Brak echa")
    time.sleep(0.5)
