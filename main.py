from machine import Pin, time_pulse_us
from time import sleep
from motors import MotorController
from position import SonicSensorsController
from vehicle import RealVehicle
from some_real_mapping_logic import MappingLogic

TRIG_FRONT = Pin(6, Pin.OUT)
TRIG_RIGHT = Pin(7, Pin.OUT)
TRIG_LEFT = Pin(8, Pin.OUT)

ECHO_FRONT = Pin(2, Pin.IN)
ECHO_RIGHT = Pin(3, Pin.IN)
ECHO_LEFT = Pin(4, Pin.IN)
"""
sonic_controller = SonicSensorsController(TRIG_FRONT, TRIG_LEFT, TRIG_RIGHT, ECHO_FRONT, ECHO_LEFT, ECHO_RIGHT)

sonic_controller.run()
"""

sleep(1)
"""
motor_controller = MotorController(
    Pin(12, Pin.OUT),
    Pin(13, Pin.OUT),
    Pin(14, Pin.OUT),
    Pin(15, Pin.OUT)
)

sleep(1)
motor_controller.test_functionality()"""

vehicle = RealVehicle()
logic = MappingLogic(vehicle)
logic.run()
#vehicle.run()