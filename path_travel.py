from directions import Direction


class PathTravel:
    def __init__(self, vehicle, path):
        self.path = path
        self.index = 0
        self.start = self.path[self.index]
        self.current_node = None
        self.dir = Direction.DOWN
        self.vehicle = vehicle
        self.pos = (self.start.x, self.start.y)

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

    def distance_to_next_node(self, current_node, next_node):
        EPSILON = 3
        if next_node.x - EPSILON < current_node.x < next_node.x + EPSILON:
            return fabs(current_node.y - next_node.y)
        elif next_node.y - EPSILON < current_node.y < next_node.y + EPSILON:
            return fabs(current_node.x - next_node.x)


    def run(self):
        self.set_direction(Direction.UP)
        self.current_node = self.start
        self.index += 1

        while self.index < len(self.path):
            next_node = self.path[self.index]

            if next_node == self.current_node.right_child:
                self.set_direction(Direction.RIGHT)
            elif next_node == self.current_node.left_child:
                self.set_direction(Direction.LEFT)
            elif next_node == self.current_node.up_child:
                self.set_direction(Direction.UP)
            elif next_node == self.current_node.down_child:
                self.set_direction(Direction.DOWN)

            self.ride_forward(self.distance_to_next_node(self.current_node, next_node), False)