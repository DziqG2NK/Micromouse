from machine import Pin
from time import sleep
from motors import MotorController
from position import SonicSensorsController


class RealVehicle():
    #States of machine
    STOPPED = "STOPPED"
    DRIVING = "DRIVING"
    TURNING = "TURNING"

    #Thresholds
    WALL_DISTANCE = 20
    COLLISION_DISTANCE = 5

    WALL = 1
    NO_WALL = 0


    def __init__(self):
        self.motor_controller = MotorController(
            AIN1 = Pin(12, Pin.OUT),
            AIN2 = Pin(13, Pin.OUT),
            BIN1 = Pin(14, Pin.OUT),
            BIN2 = Pin(15, Pin.OUT)
        )
        self.position_controller = SonicSensorsController(
            TRIG_F = Pin(6, Pin.OUT),
            TRIG_R = Pin(7, Pin.OUT),
            TRIG_L = Pin(8, Pin.OUT),
            ECHO_F = Pin(2, Pin.IN),
            ECHO_R = Pin(3, Pin.IN),
            ECHO_L = Pin(4, Pin.IN)
        )
        self.state = RealVehicle.STOPPED
        self.distances = [None, None, None]
        
        #Sensors
        self.front = "NO_WALL"
        self.left = "NO_WALL"
        self.right = "NO_WALL"


    def update_distances(self):
        self.distances = self.position_controller.get_distances()
        
        self.front = RealVehicle.WALL if self.distances[0] <= RealVehicle.COLLISION_DISTANCE else RealVehicle.NO_WALL
        self.left = RealVehicle.WALL if self.distances[1] <= RealVehicle.WALL_DISTANCE else RealVehicle.NO_WALL
        self.right = RealVehicle.WALL if self.distances[2] <= RealVehicle.WALL_DISTANCE else RealVehicle.NO_WALL

    
    def is_front_collision(self):
        return self.front
    

    def run(self):
        print("Launching the vehicle...")
        for i in range(1, 6):
            print(f"{i}...")
            sleep(1)
        
        while True:
            self.update_distances()
            
            print("Stan z przodu: ", self.is_front_collision(), self.front)

            if self.is_front_collision():
                if self.state == RealVehicle.DRIVING:
                    self.motor_controller.stop()
                    self.state = RealVehicle.STOPPED
                    print("1")
                print("2")
            
            elif not self.is_front_collision():
                if self.state == RealVehicle.STOPPED:
                    self.motor_controller.forward()
                    self.state = RealVehicle.DRIVING
                    print("3")
                print("4")
        
            sleep(0.5)

vehicle = RealVehicle()
vehicle.run()
        