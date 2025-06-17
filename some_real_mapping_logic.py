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

    # Wrappers
    def measure_distance(self, direction):
        distances = self.vehicle.position_controller.update_distances()

        if direction == Direction.LEFT:
            return distances[1]
        elif direction == Direction.UP:
            return distances[0]
        elif direction == Direction.RIGHT:
            return distances[2]

    def ride_forward(self, distance, forward=True):
        start_distance = self.measure_distance(Direction.UP)
        if forward:
            epsilon = 1
            start_left = self.measure_distance(Direction.LEFT)
            start_right = self.measure_distance(Direction.RIGHT)

        self.vehicle.ride_forward()
        while start_distance - distance < self.measure_distance(Direction.UP):
            if forward:
                left = self.measure_distance(Direction.LEFT)
                right = self.measure_distance(Direction.RIGHT)
                if left < start_left - epsilon:
                    start_left = left
                if right < start_right - epsilon:
                    start_right = right

                if right - epsilon > WALL_THRESHOLD:
                    self.vehicle.stop()
                    return False
                if left - epsilon > WALL_THRESHOLD:
                    self.vehicle.stop()
                    return False


        self.vehicle.stop()
        return True

    def turn(self, direction):
        if direction == Direction.LEFT:
            self.vehicle.turn_left()
            self.dir = Direction((self.dir.value - 1) % 4)
        elif direction == Direction.UP:
            pass
        elif direction == Direction.RIGHT:
            self.vehicle.turn_right()
            self.dir = Direction((self.dir.value + 1) % 4)

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


    # OG Logic (using wrappers)
    def create_start_node(self):
        self.start = Node()

    def first_free_direction(self, current_node):
        for direction in [Direction.LEFT, Direction.UP, Direction.RIGHT]:
            if self.measure_distance(direction) > WALL_THRESHOLD:
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
        self.ride_forward(distance - DISTANCE_TO_WALL, True)
        return current_node.create_child(self.dir)

    def backtrack(self, current_node):
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



