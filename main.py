from machine import Pin, time_pulse_us
from motors import some_fun
import time

"""
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
from machine import Pin, PWM
from time import sleep


class MotorController():

    MIN_DUTY = 0
    MAX_DUTY = 65535
    MOVEMENT_DUTY = 54000
    ROTATION_DUTY = 52000

    # Pins BIN1, BIN2 handles LEFT motor motion
    # Pins AIN1, AIN2 handles RIGHT motor motion

    def __init__(self, AIN1: Pin, AIN2: Pin, BIN1: Pin, BIN2: Pin, frequency=20000):
        self.AIN1 = PWM(AIN1)
        self.AIN2 = PWM(AIN2)
        self.BIN1 = PWM(BIN1)
        self.BIN2 = PWM(BIN2)
        
        self.AIN1.freq(frequency)
        self.AIN2.freq(frequency)
        self.BIN1.freq(frequency)
        self.BIN2.freq(frequency)
        
        
    def stop(self):
        self.AIN1.duty_u16(MotorController.MIN_DUTY)
        self.AIN2.duty_u16(MotorController.MIN_DUTY)
        
        self.BIN1.duty_u16(MotorController.MIN_DUTY)
        self.BIN2.duty_u16(MotorController.MIN_DUTY)
        
        print("Engines stopped")
        
    def right(self):
        self.AIN1.duty_u16(MotorController.ROTATION_DUTY)
        self.AIN2.duty_u16(MotorController.MIN_DUTY)
        
        self.BIN1.duty_u16(MotorController.ROTATION_DUTY)
        self.BIN2.duty_u16(MotorController.MIN_DUTY)
        
        print("Turning right")
        
        
    def left(self):
        self.AIN1.duty_u16(MotorController.MIN_DUTY)
        self.AIN2.duty_u16(MotorController.ROTATION_DUTY)
        
        self.BIN1.duty_u16(MotorController.MIN_DUTY)
        self.BIN2.duty_u16(MotorController.ROTATION_DUTY)
        
        print("Turning left")


    def forward(self):
        self.AIN1.duty_u16(MotorController.MIN_DUTY)
        self.AIN2.duty_u16(MotorController.MOVEMENT_DUTY)
        
        self.BIN1.duty_u16(MotorController.MOVEMENT_DUTY)
        self.BIN2.duty_u16(MotorController.MIN_DUTY)
        
        print("Driving forward")
        

    def change_right_motor_speed(self):


        PWM_AIN1 = PWM(Pin(14, Pin.OUT))
        AIN2_pin = Pin(15, Pin.OUT)
        AIN2_pin.value(0)

        pin_12 = Pin(12, Pin.OUT)
        pin_13 = Pin(13, Pin.OUT)

        print("Start")

        for duty in range(0, 65536, 1000):
            PWM_AIN1.duty_u16(duty)
            
            print(duty)
            print(PWM_AIN1.duty_u16(), AIN2_pin.value(), pin_12.value(), pin_13.value())
            
            sleep(0.1)

        for duty in range(65536, 0, -1000):
            PWM_AIN1.duty_u16(duty)

            print(duty)
            print(PWM_AIN1.duty_u16(), AIN2_pin.value(), pin_12.value(), pin_13.value())

            sleep(0.1)

        
    def log(self):
        print(self.AIN1.duty_u16())
        print(self.AIN2.duty_u16())
        print(self.BIN1.duty_u16())
        print(self.BIN2.duty_u16())

        
    def test_functionality(self):
        
        
        print("right")
        self.right()
        print("wait")
        self.log()
        sleep(5)
        
        print("left")
        self.left()
        print("wait")
        self.log()
        sleep(5)
        
        print("forward")
        self.forward()
        print("wait")
        self.log()
        sleep(5)
        
        print("stop")
        self.stop()
        
        
        """
        pin_14 = Pin(14, Pin.OUT)
        pin_15 = Pin(15, Pin.OUT)
        
    
        pin_14.value(1)
        pin_15.value(0)
        print("Pin 14: 1, Pin 15: 0")
        self.log()
        sleep(3)


        pin_14.value(0)
        pin_15.value(1)
        print("Pin 14: 0, Pin 15: 1")
        sleep(3)
        

        
        print("BFJNDKNJ")
        self.change_right_motor_speed()

        self.stop()
        
        pin_14.value(0)
        pin_15.value(0)
        """
        
   
        
        
        
    
#left(AIN1, AIN2, BIN1, BIN2)

#forward(AIN1, AIN2, BIN1, BIN2)
#right(AIN1, AIN2, BIN1, BIN2)
#right(PWM_AIN1, PWM_AIN2, BIN1, BIN2)
#right(PWM_AIN1, PWM_AIN2, BIN1, BIN2)
#right(PWM_AIN1, PWM_AIN2, BIN1, BIN2)
#right(AIN1, AIN2, BIN1, BIN2)
#stop(AIN1, AIN2, BIN1, BIN2)


#change_right_motor_speed(AIN1, AIN2)
        

motor_controller = MotorController(
    Pin(12, Pin.OUT),
    Pin(13, Pin.OUT),
    Pin(14, Pin.OUT),
    Pin(15, Pin.OUT)
)

motor_controller.test_functionality()
