from math import sin, cos
from directions import Direction

class Vehicle:
    def __init__(self, sensor_left, sensor_up, sensor_right):
        self.x = 0
        self.y = 0
        self.dir = Direction.UP
        self.sensor_left = sensor_left
        self.sensor_up = sensor_up
        self.sensor_right = sensor_right

    def measure_distance(self, direction):
        if direction == Direction.UP:
            return self.sensor_up.measure()
        elif direction == Direction.RIGHT:
            return self.sensor_right.measure()
        elif direction == Direction.LEFT:
            return self.sensor_left.measure()

    def ride_forward(self, distance):
        start_dist = self.measure_distance(Direction.UP)
        while self.measure_distance(Direction.UP) < start_dist - distance:
            # TODO: Obsługa silnika
            # Kod zakłada że łazik jedzie idealnie w lini prostej i nie wykryje jeżeli zacznie zbliżać się do ściany.
            pass

    def turn(self, direction):
        degrees_to_turn = (direction.value - self.dir.value) * 90

        # TODO: Obsługa silnika


    def set_pos(self, x, y):
        self.x = x
        self.y = y