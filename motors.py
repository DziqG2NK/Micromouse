from machine import Pin, PWM
from time import sleep

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
    
    time.sleep(0.5)
    
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

    print("A:")
    print(AIN1.value(), AIN2.value())

    print("B:")
    print(BIN1.value(), BIN2.value())

    sleep(0.1)
    
    stop(AIN1_pin, AIN2_pin, BIN1_pin, BIN2_pin)

def forward(AIN1_pin, AIN2_pin, BIN1_pin, BIN2_pin):
    AIN1.value(0)
    AIN2.value(1)
    
    BIN1.value(1)
    BIN2.value(0)
    
    print("Driving forward")

    print("A:")
    print(AIN1.value(), AIN2.value())

    print("B:")
    print(BIN1.value(), BIN2.value())

    sleep(0.5)
    
    stop(AIN1_pin, AIN2_pin, BIN1_pin, BIN2_pin)

#right(AIN1, AIN2, BIN1, BIN2)

#time.sleep(1)

#right(AIN1, AIN2, BIN1, BIN2)

def change_right_motor_speed(AIN1_pin, AIN2_pin):
    PWM_AIN1 = PWM(AIN1_pin)
    AIN2_pin.value(0)

    print("Start")

    for duty in range(0, 65536, 2000):
        PWM_AIN1.duty_u16(duty)
        
        sleep(0.1)

    for duty in range(65536, 0, -500):
        PWM_AIN1.duty_u16(duty)

        sleep(0.1)
        
    print("Stop")
    stop(AIN1, AIN2, BIN1, BIN2)

#left(AIN1, AIN2, BIN1, BIN2)

#forward(AIN1, AIN2, BIN1, BIN2)
#right(AIN1, AIN2, BIN1, BIN2)
#right(PWM_AIN1, PWM_AIN2, BIN1, BIN2)
#right(PWM_AIN1, PWM_AIN2, BIN1, BIN2)
#right(PWM_AIN1, PWM_AIN2, BIN1, BIN2)
#right(PWM_AIN1, PWM_AIN2, BIN1, BIN2)

change_right_motor_speed(AIN1, AIN2)