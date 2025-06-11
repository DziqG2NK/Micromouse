from math import sin, cos
from directions import Direction
from globals import WALL_THRESHOLD


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

    def all_measurements(self):
        return self.sensor_left.measure(), self.sensor_up.measure(), self.sensor_right.measure()


    def ride_forward(self, distance, check_for_road=False):
        # Na ten moment taki kod do testowania symulacji, bo nie obsługuje silnika.
        if self.is_simulation:
            start = True

            while distance > 0:
                if check_for_road:
                    if start:
                        measurement_l, measurement_u, measurement_r = self.all_measurements()
                        start = False

                    measurement_u = self.measure_distance(Direction.UP)

                    if measurement_u > WALL_THRESHOLD:
                        measurement_l = min(self.measure_distance(Direction.LEFT), measurement_l)
                        measurement_r = min(self.measure_distance(Direction.RIGHT), measurement_r)
                        if measurement_l < self.measure_distance(Direction.LEFT) or measurement_r < self.measure_distance(Direction.RIGHT):
                            return False

                if self.dir == Direction.UP:
                    self.y -= 1
                elif self.dir == Direction.RIGHT:
                    self.x += 1
                elif self.dir == Direction.DOWN:
                    self.y += 1
                elif self.dir == Direction.LEFT:
                    self.x -= 1
                distance -= 1
            return True

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

    def turn_left(self, epsilon=0.1):
        if self.is_simulation:
            self.set_direction(Direction((self.dir.value - 1) % 4), epsilon)
            return

        # TODO: Obsługa silnika

    def turn_right(self, epsilon=0.1):
        if self.is_simulation:
            self.set_direction(Direction((self.dir.value + 1) % 4), epsilon)
            return

        # TODO: Obsługa silnika

    def turn_around(self, epsilon=0.1):
        if self.is_simulation:
            self.set_direction(Direction((self.dir.value + 2) % 4), epsilon)
            return

        # TODO: Obsługa silnika

    def turn(self, direction):
        if direction == Direction.LEFT:
            self.turn_left()
        elif direction == Direction.RIGHT:
            self.turn_right()
        elif direction == Direction.UP:
            pass
        else:
            raise ValueError("Invalid direction. Use Direction.LEFT or Direction.RIGHT.")

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def get_pos(self):
        return self.x, self.y

    def you_are_in_the_Matrix_Neo(self):
        self.is_simulation = True