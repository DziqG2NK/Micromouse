from some_real_mapping_node import Node
from directions import Direction
from globals import *
# import _thread

class MappingLogic:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.start = None
        self.path = []
        self.dir = Direction.UP  # Default direction
        self.pos = (0, 0)

    # Wrappers
    def measure_distance(self, direction):
        distances = self.vehicle.position_controller.update_distances()

        if direction == Direction.LEFT:
            return distances[1]
        elif direction == Direction.UP:
            return distances[0]
        elif direction == Direction.RIGHT:
            return distances[2]

    def ride_forward(self, distance, check_for_corridors=True):
        start_distance = self.measure_distance(Direction.UP)
        if check_for_corridors:
            epsilon = 1
            start_left = self.measure_distance(Direction.LEFT)
            start_right = self.measure_distance(Direction.RIGHT)

        self.vehicle.motor_controller.forward()
        while start_distance - distance < self.measure_distance(Direction.UP):
            if check_for_corridors:
                left = self.measure_distance(Direction.LEFT)
                right = self.measure_distance(Direction.RIGHT)
                if left < start_left - epsilon:
                    start_left = left
                if right < start_right - epsilon:
                    start_right = right

                if right - epsilon > self.vehicle.WALL_DISTANCE:
                    self.vehicle.motor_controller.stop()
                    traveled_distance = start_distance - self.measure_distance(Direction.UP)
                    self.update_pos(traveled_distance)
                    return False
                if left - epsilon > self.vehicle.WALL_DISTANCE:
                    self.vehicle.motor_controller.stop()
                    traveled_distance = start_distance - self.measure_distance(Direction.UP)
                    self.update_pos(traveled_distance)
                    return False

        self.vehicle.motor_controller.stop()
        self.update_pos(distance)
        return True

    def turn_left(self):
        up_distance = self.measure_distance(Direction.UP)
        done = False
        while not done:
            done = self.vehicle.motor_controller.turn_left(done, self.measure_distance(Direction.RIGHT), up_distance)

        self.dir = Direction((self.dir.value - 1) % 4)

    def turn_right(self):
        up_distance = self.measure_distance(Direction.UP)
        done = False
        while not done:
            done = self.vehicle.motor_controller.turn_right(done, self.measure_distance(Direction.LEFT), up_distance)

        self.dir = Direction((self.dir.value - 1) % 4)

    def turn(self, direction):
        if direction == Direction.LEFT:
            self.turn_left()
        elif direction == Direction.UP:
            pass
        elif direction == Direction.RIGHT:
            self.turn_right()

    def set_direction(self, direction):
        times_to_turn_right = (direction.value - self.dir.value) % 4
        times_to_turn_left = (self.dir.value - direction.value) % 4
        if times_to_turn_right < times_to_turn_left:
            for _ in range(times_to_turn_right):
                self.turn(Direction.RIGHT)
        else:
            for _ in range(times_to_turn_left):
                self.turn(Direction.LEFT)

        self.dir = direction

    def update_pos(self, distance):
        if self.dir == Direction.UP:
            self.pos = (self.pos[0], self.pos[1] - distance)
        elif self.dir == Direction.LEFT:
            self.pos = (self.pos[0] - distance, self.pos[1])
        elif self.dir == Direction.RIGHT:
            self.pos = (self.pos[0] + distance, self.pos[1])
        elif self.dir == Direction.DOWN:
            self.pos = (self.pos[0], self.pos[1] + distance)


    # OG Logic (using wrappers)
    def create_start_node(self):
        self.start = Node(*self.pos)

    def first_free_direction(self, current_node):
        for direction in [Direction.LEFT, Direction.UP, Direction.RIGHT]:
            if self.measure_distance(direction) > self.vehicle.WALL_DISTANCE:
                dir = Direction((direction.value + self.dir.value) % 4)
                if not current_node.does_child_exist(dir):
                    return direction
        return None

    def run_cycle(self, current_node):
        direction = self.first_free_direction(current_node)
        if direction is None:
            return self.backtrack(current_node)
        self.path.append(current_node)
        distance = self.measure_distance(direction)
        self.turn(direction)
        self.ride_forward(distance - self.vehicle.COLLISION_DISTANCE, True)
        return current_node.create_child(self.dir, *self.pos)

    def backtrack(self, current_node):
        if not self.path:
            return None
        parent_node = self.path.pop()

        if parent_node.x < current_node.x:
            self.set_direction(Direction.LEFT)
        elif parent_node.x > current_node.x:
            self.set_direction(Direction.RIGHT)
        elif parent_node.y < current_node.y:
            self.set_direction(Direction.UP)
        elif parent_node.y > current_node.y:
            self.set_direction(Direction.DOWN)

        # Calculate the distance to the parent node
        distance = fabs(current_node.x - parent_node.x) + fabs(current_node.y - parent_node.y)

        # Move the vehicle to the parent node
        self.ride_forward(distance, False)

        # Return the parent node
        return parent_node


    def run(self):
        if self.start is None:
            self.create_start_node()

        current_node = self.start
        while True:
            new_node = self.run_cycle(current_node)
            if new_node is None:
                break
            current_node = new_node
