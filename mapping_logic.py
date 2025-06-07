from mapping_node import Node
from directions import Direction

WALL_DISTANCE = 3 # Dystans w cm od ściany, przy którym łazik uznaje, że nie ma już miejsca na jazdę.


class MappingLogic:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.start = None

    def create_start_node(self):
        self.start = Node(*self.vehicle.get_pos())

    def first_free_direction(self, current_node):
        for direction in [Direction.LEFT, Direction.UP, Direction.RIGHT]:
            if self.vehicle.measure_distance(direction) > WALL_DISTANCE:
                dir = Direction((direction.value + self.vehicle.dir.value) % 4)
                if not current_node.does_child_exist(dir):
                    return direction
        return None

    def run_cycle(self, current_node):
        direction = self.first_free_direction(current_node)
        if direction is None:
            return None
        distance = self.vehicle.measure_distance(direction)
        self.vehicle.turn(direction)
        self.vehicle.ride_forward(distance - WALL_DISTANCE)
        return current_node.create_child(self.vehicle.dir, distance - WALL_DISTANCE)


    def run(self):
        if self.start is None:
            self.create_start_node()

        current_node = self.start
        while True:
            new_node = self.run_cycle(current_node)
            if new_node is None:
                break
            current_node = new_node



