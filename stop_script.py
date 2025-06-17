from motors import MotorController
from machine import Pin

motor_controller = MotorController(
    Pin(12, Pin.OUT),
    Pin(13, Pin.OUT),
    Pin(14, Pin.OUT),
    Pin(15, Pin.OUT)
)

motor_controller.stop()