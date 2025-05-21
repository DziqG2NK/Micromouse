from machine import Pin, time_pulse_us
import time

class Sensor:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger = Pin(trigger_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)

    def measure(self):
        self.trigger.low()
        time.sleep_us(2)
        self.trigger.high()
        time.sleep_us(10)
        self.trigger.low()

        # Measure echo pulse width
        duration = time_pulse_us(self.echo, 1, 30000)  # 30 ms timeout
        if duration < 0:
            return None  # timeout

        distance_cm = duration / 58.0  # według dokumentacji SRF05
        return distance_cm