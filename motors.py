from machine import Pin
import time

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
    
def forward(AIN1_pin, AIN2_pin, BIN1_pin, BIN2_pin):
    AIN1.value(1)
    AIN2.value(0)
    
    BIN1.value(1)
    BIN2.value(0)
    
    time.sleep(0.1)
    
    AIN1.value(0)
    AIN2.value(0)

    BIN1.value(0)
    BIN2.value(0)

forward(AIN1, AIN2, BIN1, BIN2)
