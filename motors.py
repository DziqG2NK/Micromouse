from machine import Pin, PWM
from time import sleep
from math import fabs

class MotorController():

    MIN_DUTY = 0
    MAX_DUTY = 65535
    MOVEMENT_DUTY = 54000 #59000
    ROTATION_DUTY = 50000 #51000
    
    # in centimeters
    ROTATION_DISTANCE_TOLERANCE = 2.5

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
        
        print("Turning RIGHT")
        
        
    def left(self):
        self.AIN1.duty_u16(MotorController.MIN_DUTY)
        self.AIN2.duty_u16(MotorController.ROTATION_DUTY)
        
        self.BIN1.duty_u16(MotorController.MIN_DUTY)
        self.BIN2.duty_u16(MotorController.ROTATION_DUTY)
        
        print("Turning LEFT")


    def forward(self):
        self.AIN1.duty_u16(MotorController.MIN_DUTY)
        self.AIN2.duty_u16(MotorController.MOVEMENT_DUTY)
        
        self.BIN1.duty_u16(MotorController.MOVEMENT_DUTY)
        self.BIN2.duty_u16(MotorController.MIN_DUTY)
        
        print("Driving forward")
        
        
    def is_in_tolerance(self, proper_distance, new_distance):
        if proper_distance is None:
            return new_distance is None
            
        diff = fabs(proper_distance -new_distance)
        
        return diff <= MotorController.ROTATION_DISTANCE_TOLERANCE


    # Returns if turning left manouver has ended
    def turn_left(self, is_already_turning, right_sensor_distance, const_front_sensor_distance):
        
        if not is_already_turning:
            print("PRZED")
            self.left()
            print("PO")
            sleep(1.2)
            return True
        else:
            print("WARTOŚCI DO ZATRZYMANIA SKRETU: ", const_front_sensor_distance, right_sensor_distance)
            if self.is_in_tolerance(const_front_sensor_distance, right_sensor_distance):
                self.stop()
                raise ValueError()
                return False
            return True
    
    def turn_right(self, is_already_turning, left_sensor_distance, const_front_sensor_distance):
    
        if not is_already_turning:
            print("PRZED")
            self.right()
            print("PO")
            sleep(1.2)
            return True
        else:
            print("WARTOŚCI DO ZATRZYMANIA SKRETU: ", const_front_sensor_distance, left_sensor_distance)
            if self.is_in_tolerance(const_front_sensor_distance, left_sensor_distance):
                self.stop()
                raise ValueError()
                return False
            return True

        
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



