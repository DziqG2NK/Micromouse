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
        self.is_simulation = False

    def measure_distance(self, direction):
        if direction == Direction.UP:
            return self.sensor_up.measure()
        elif direction == Direction.RIGHT:
            return self.sensor_right.measure()
        elif direction == Direction.LEFT:
            return self.sensor_left.measure()

    def ride_forward(self, distance):
        # Na ten moment taki kod do testowania symulacji, bo nie obsługuje silnika.
        if self.is_simulation:
            if self.dir == Direction.UP:
                self.y -= distance
            elif self.dir == Direction.RIGHT:
                self.x += distance
            elif self.dir == Direction.DOWN:
                self.y += distance
            elif self.dir == Direction.LEFT:
                self.x -= distance
            return

        start_dist = self.measure_distance(Direction.UP)
        while self.measure_distance(Direction.UP) < start_dist - distance:
            # TODO: Obsługa silnika
            # Kod zakłada że łazik jedzie idealnie w lini prostej i nie wykryje jeżeli zacznie zbliżać się do ściany.
            pass

    def set_direction(self, direction, epsilon= 0.1):
        # Na ten moment taki kod do testowania symulacji, bo nie obsługuje silnika.
        if self.is_simulation:
            self.dir = direction
            return

        degrees_to_turn = (direction.value - self.dir.value) * 90

        m_left = self.measure_distance(Direction.LEFT)
        m_up = self.measure_distance(Direction.UP)
        m_right = self.measure_distance(Direction.RIGHT)

        # TODO: Obsługa silnika




        self.dir = direction


    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def you_are_in_the_Matrix_Neo(self):
        self.is_simulation = True