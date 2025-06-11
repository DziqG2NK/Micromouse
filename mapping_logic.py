from mapping_node import Node
from directions import Direction

WALL_THRESHOLD = 7 # Dystans w cm od ściany, przy którym łazik uznaje, że ma dalszych rozgałęzień do eksploracji.
DISTANCE_TO_WALL = 3 # Dystans w cm od ściany, przy którym łazik uznaje, że nie ma już miejsca na jazdę.

class MappingLogic:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.start = None
        self.path = []

    def create_start_node(self):
        self.start = Node(*self.vehicle.get_pos())

    def first_free_direction(self, current_node):
        for direction in [Direction.LEFT, Direction.UP, Direction.RIGHT]:
            if self.vehicle.measure_distance(direction) > WALL_THRESHOLD:
                dir = Direction((direction.value + self.vehicle.dir.value) % 4)
                if not current_node.does_child_exist(dir):
                    return direction
        return None

    def run_cycle(self, current_node):
        direction = self.first_free_direction(current_node)
        if direction is None:
            return self.backtrack(current_node)
        self.path.append(current_node)
        distance = self.vehicle.measure_distance(direction)
        self.vehicle.turn(direction)
        self.vehicle.ride_forward(distance - DISTANCE_TO_WALL)
        return current_node.create_child(self.vehicle.dir, distance - DISTANCE_TO_WALL)

    def backtrack(self, current_node):
        parent_node = self.path.pop()

        if parent_node.x < current_node.x:
            self.vehicle.set_direction(Direction.LEFT)
        elif parent_node.x > current_node.x:
            self.vehicle.set_direction(Direction.RIGHT)
        elif parent_node.y < current_node.y:
            self.vehicle.set_direction(Direction.UP)
        elif parent_node.y > current_node.y:
            self.vehicle.set_direction(Direction.DOWN)

        # Calculate the distance to the parent node
        distance = abs(current_node.x - parent_node.x) + abs(current_node.y - parent_node.y)

        # Move the vehicle to the parent node
        self.vehicle.ride_forward(distance)

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



