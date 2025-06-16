from machine import Pin, PWM
from time import sleep


"""
class MotorController():

    MIN_DUTY = 0
    MOVEMENT_DUTY = 45000
    ROTATION_DUTY = 40000

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
        
        pin12 = Pin(12, Pin.OUT)
        pin13 = Pin(13, Pin.OUT)
        pin14 = Pin(14, Pin.OUT)
        pin15 = Pin(15, Pin.OUT)
        
        pin12.value(0)
        pin13.value(0)
        pin14.value(0)
        pin15.value(0)
        
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
        
        #print("A:")
        #print(AIN1.value(), AIN2.value())

        #print("B:")
        #print(BIN1.value(), BIN2.value())
        

    def change_right_motor_speed(self):


        PWM_AIN1 = PWM(Pin(14, Pin.OUT))
        AIN2_pin = Pin(13, Pin.OUT)
        AIN2_pin.value(0)

        print("Start")

        for duty in range(0, 65536, 2000):
            PWM_AIN1.duty_u16(duty)
            
            sleep(0.1)

        for duty in range(65536, 0, -500):
            PWM_AIN1.duty_u16(duty)

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
        self.left()
        print("wait")
        self.log()
        sleep(5)
        
        print("stop")
        self.stop()
        
        #break
        self.forward()
        
        self.log()

        
        sleep(5)


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
        
"""
motor_controller = MotorController(
    Pin(12, Pin.OUT),
    Pin(13, Pin.OUT),
    Pin(14, Pin.OUT),
    Pin(15, Pin.OUT)
)

motor_controller.test_functionality()

"""

AIN1 = Pin(12, Pin.OUT)
AIN2 = Pin(13, Pin.OUT)

BIN1 = Pin(14, Pin.OUT)
BIN2 = Pin(15, Pin.OUT)

"""
while True:
    pin_14.value(1)
    pin_15.value(0)
    print("Pin 14: 1, Pin 15: 0")
    time.sleep(3)


    pin_14.value(0)
    pin_15.value(1)
    print("Pin 14: 0, Pin 15: 1")
    time.sleep(3)"""
    
def stop(AIN1_pin, AIN2_pin, BIN1_pin, BIN2_pin):
    AIN1.value(0)
    AIN2.value(0)
    
    BIN1.value(0)
    BIN2.value(0)
    
    print("Engines stopped")
    
    
def right(AIN1_pin, AIN2_pin, BIN1_pin, BIN2_pin):
    AIN1.value(1)
    AIN2.value(0)
    
    BIN1.value(1)
    BIN2.value(0)
    
    print("Turning right")
    
    sleep(0.5)
    
    stop(AIN1_pin, AIN2_pin, BIN1_pin, BIN2_pin)

def left(AIN1_pin, AIN2_pin, BIN1_pin, BIN2_pin):
    AIN1.value(0)
    AIN2.value(1)
    
    BIN1.value(0)
    BIN2.value(1)
    
    print("Turning left")

    sleep(0.5)
    
    stop(AIN1_pin, AIN2_pin, BIN1_pin, BIN2_pin)

def rotate_back(AIN1_pin, AIN2_pin, BIN1_pin, BIN2_pin):
    AIN1.value(0)
    AIN2.value(1)
    
    BIN1.value(0)
    BIN2.value(1)
    
    print("Turning back")

    sleep(0.1)
    
    stop(AIN1_pin, AIN2_pin, BIN1_pin, BIN2_pin)

def forward(AIN1_pin, AIN2_pin, BIN1_pin, BIN2_pin):
    AIN1.value(0)
    AIN2.value(1)
    
    BIN1.value(1)
    BIN2.value(0)
    
    print("Driving forward")

    sleep(0.5)
    
    stop(AIN1_pin, AIN2_pin, BIN1_pin, BIN2_pin)


right(AIN1, AIN2, BIN1, BIN2)

sleep(2)

left(AIN1, AIN2, BIN1, BIN2)

forward(AIN1, AIN2, BIN1, BIN2)
