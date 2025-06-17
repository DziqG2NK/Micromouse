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
        

motor_controller = MotorController(
    Pin(12, Pin.OUT),
    Pin(13, Pin.OUT),
    Pin(14, Pin.OUT),
    Pin(15, Pin.OUT)
)

motor_controller.test_functionality()
