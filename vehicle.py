from machine import Pin
from time import sleep
from motors import MotorController
from position import SonicSensorsController


class Vehicle():
    #States of machine
    STOPPED = "STOPPED"
    DRIVING = "DRIVING"
    TURNING = "TURNING"

    #Thresholds
    WALL_DISTANCE = 12
    COLLISION_DISTANCE = 12

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
        self.state = Vehicle.STOPPED
        self.distances = [None, None, None]
        
        #Sensors
        self.front = "NO_WALL"
        self.left = "NO_WALL"
        self.right = "NO_WALL"
        
        self.is_already_turning = False


    def update_distances(self):
        self.distances = self.position_controller.get_distances()
        
        if self.distances[0] is None:
            self.front = Vehicle.NO_WALL
        elif self.distances[0] <= Vehicle.COLLISION_DISTANCE:
            self.front = Vehicle.WALL
        else:
            self.front = Vehicle.NO_WALL

        # left
        if self.distances[1] is None:
            self.left = Vehicle.NO_WALL
        elif self.distances[1] <= Vehicle.WALL_DISTANCE:
            self.left = Vehicle.WALL
        else:
            self.left = Vehicle.NO_WALL

        # right
        if self.distances[2] is None:
            self.right = Vehicle.NO_WALL
        elif self.distances[2] <= Vehicle.WALL_DISTANCE:
            self.right = Vehicle.WALL
        else:
            self.right = Vehicle.NO_WALL

    
    def is_front_collision(self):
        return self.front
    

    def get_free_direction(self):
        if self.distances[1] > Vehicle.WALL_DISTANCE:
            return "LEFT"
        
        elif self.distances[0] > Vehicle.COLLISION_DISTANCE:
            return "FRONT"
        
        elif self.distances[2] > Vehicle.WALL_DISTANCE:
            return "RIGHT"
        
        else:
            return None


    def run(self):
        try:
            print("Launching the vehicle...")
            for i in range(1, 2):
                print(f"{i}...")
                sleep(1)
            
            const_value_to_turn = None
            direction = None
            
            while True:
                self.update_distances()

                if not self.is_already_turning:
                    if self.is_front_collision():
                        
                        print(self.front, self.state)
                        
                        if self.state == Vehicle.DRIVING:
                            self.motor_controller.stop()
                            self.state = Vehicle.STOPPED
                            print("1")
                        
                        if self.state == Vehicle.STOPPED:
                            direction = self.get_free_direction()
                            print(direction)
                            
                            if direction is None:
                                print("COŚ POSZŁO NIE TAK")
                                self.motor_controller.stop()
                                return

                            elif direction == "LEFT" or direction == "RIGHT":
                                const_value_to_turn = self.distances[0]
                                
                                self.state = Vehicle.TURNING
                                
                                if direction == "LEFT":
                                    self.motor_controller.turn_left(self.is_already_turning, self.distances[2], const_value_to_turn)
                                    
                                elif direction == "RIGHT":
                                    self.motor_controller.turn_right(self.is_already_turning, self.distances[1], const_value_to_turn)
                                    
                                self.is_already_turning = True

                            elif direction == "FRONT":
                                print("COŚ POSZŁO NIE TAK")
                                self.motor_controller.stop()
                                return
                            
                            print("2")
                        
                    
                    elif not self.is_front_collision():
                        if self.state == Vehicle.STOPPED:
                            self.motor_controller.forward()
                            self.state = Vehicle.DRIVING
                            print("3")
                        print("4")
                
                    sleep(0.25)

                else:
                    if direction == "RIGHT":
                        if self.motor_controller.turn_right(self.is_already_turning, self.distances[1], const_value_to_turn):
                            self.state = Vehicle.DRIVING
                            direction = None
                            self.is_already_turning = False
                            self.motor_controller.forward()
                            
                    elif direction == "LEFT":
                        if self.motor_controller.turn_left(self.is_already_turning, self.distances[2], const_value_to_turn):
                            self.state = Vehicle.DRIVING
                            direction = None
                            self.is_already_turning = False
                            self.motor_controller.forward()
                            
                    sleep(0.02)
                
        finally:
            self.motor_controller.stop()

