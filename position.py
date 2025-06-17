from machine import Pin, time_pulse_us
import time

class SonicSensorsController():

    def __init__(self, TRIG_F, TRIG_L, TRIG_R, ECHO_F, ECHO_L, ECHO_R):
        self.TRIG_F = TRIG_F
        self.TRIG_L = TRIG_L
        self.TRIG_R = TRIG_R
        
        self.ECHO_F = ECHO_F
        self.ECHO_L = ECHO_L
        self.ECHO_R = ECHO_R

        self.elems = [
            (TRIG_F, ECHO_F),
            (TRIG_L, ECHO_L),
            (TRIG_R, ECHO_R)
        ]

    def measure_distance(self, trigger, echo):

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


    def get_distances(self):
        measurements = [None, None, None]
        for i, (trigger, echo) in enumerate(self.elems):
            measurements[i] = self.measure_distance(trigger, echo)
        
        if measurements[0] is not None:
            print("Odległość przedniego: {:.2f} cm".format(measurements[0]))

        elif measurements[1] is not None:
            print("Odległość lewego: {:.2f} cm".format(measurements[1]))
            
        elif measurements[2] is not None:
            print("Odległość prawego: {:.2f} cm".format(measurements[2]))
        
        else:
            print("Brak echa")
        
        return measurements


    def run(self):
        while True:
            measurements = [None, None, None]
            for i, (trigger, echo) in enumerate(self.elems):
                measurements[i] = self.measure_distance(trigger, echo)
            
            if measurements[0] is not None and measurements[1] is not None:
                print("Odległość przedniego: {:.2f} cm".format(measurements[0]))
                print("Odległość lewego: {:.2f} cm".format(measurements[1]))
                print("Odległość prawego: {:.2f} cm".format(measurements[2]))
            else:
                print("Brak echa")
            time.sleep(0.5)
