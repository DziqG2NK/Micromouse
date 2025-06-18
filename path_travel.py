from real_direction import Direction


class PathTravel:
    def __init__(self, vehicle, path):
        self.path = path
        self.index = 0
        self.start = self.path[self.index]
        self.current_node = None
        self.dir = Direction("DOWN")
        self.vehicle = vehicle
        self.pos = (self.start.x, self.start.y)

        # Wrappers

    def measure_distance(self, direction):
        distances = self.vehicle.position_controller.update_distances()

        if direction == "LEFT":
            return distances[1]
        elif direction == "UP":
            return distances[0]
        elif direction == "RIGHT":
            return distances[2]

    def ride_forward(self, distance, check_for_corridors=True):
        start_distance = self.measure_distance("UP")
        if check_for_corridors:
            epsilon = 1
            start_left = self.measure_distance("LEFT")
            start_right = self.measure_distance("RIGHT")

        self.vehicle.motor_controller.forward()
        while start_distance - distance < self.measure_distance("UP"):
            if check_for_corridors:
                left = self.measure_distance("LEFT")
                right = self.measure_distance("RIGHT")
                if left < start_left - epsilon:
                    start_left = left
                if right < start_right - epsilon:
                    start_right = right

                if right - epsilon > self.vehicle.WALL_DISTANCE:
                    self.vehicle.motor_controller.stop()
                    traveled_distance = start_distance - self.measure_distance("UP")
                    self.update_pos(traveled_distance)
                    return False
                if left - epsilon > self.vehicle.WALL_DISTANCE:
                    self.vehicle.motor_controller.stop()
                    traveled_distance = start_distance - self.measure_distance("UP")
                    self.update_pos(traveled_distance)
                    return False

        self.vehicle.motor_controller.stop()
        self.update_pos(distance)
        return True

    def turn_left(self):
        up_distance = self.measure_distance("UP")
        done = False
        while not done:
            done = self.vehicle.motor_controller.turn_left(done, self.measure_distance("RIGHT"), up_distance)

        self.dir -= 1

    def turn_right(self):
        up_distance = self.measure_distance("UP")
        done = False
        while not done:
            done = self.vehicle.motor_controller.turn_right(done, self.measure_distance("LEFT"), up_distance)

        self.dir += 1

    def turn(self, direction):
        if direction == "LEFT":
            self.turn_left()
        elif direction == "UP":
            pass
        elif direction == "RIGHT":
            self.turn_right()

    def set_direction(self, direction):
        times_to_turn_right = direction - self.dir
        times_to_turn_left = self.dir - direction
        if times_to_turn_right < times_to_turn_left:
            for _ in range(times_to_turn_right):
                self.turn("RIGHT")
        else:
            for _ in range(times_to_turn_left):
                self.turn("LEFT")

        self.dir = Direction(direction)

    def update_pos(self, distance):
        if self.dir == "UP":
            self.pos = (self.pos[0], self.pos[1] - distance)
        elif self.dir == "LEFT":
            self.pos = (self.pos[0] - distance, self.pos[1])
        elif self.dir == "RIGHT":
            self.pos = (self.pos[0] + distance, self.pos[1])
        elif self.dir == "DOWN":
            self.pos = (self.pos[0], self.pos[1] + distance)

    def distance_to_next_node(self, current_node, next_node):
        EPSILON = 3
        if next_node.x - EPSILON < current_node.x < next_node.x + EPSILON:
            return fabs(current_node.y - next_node.y)
        elif next_node.y - EPSILON < current_node.y < next_node.y + EPSILON:
            return fabs(current_node.x - next_node.x)


    def run(self):
        self.set_direction("UP")
        self.current_node = self.start
        self.index += 1

        while self.index < len(self.path):
            next_node = self.path[self.index]

            if next_node == self.current_node.right_child:
                self.set_direction("RIGHT")
            elif next_node == self.current_node.left_child:
                self.set_direction("LEFT")
            elif next_node == self.current_node.up_child:
                self.set_direction("UP")
            elif next_node == self.current_node.down_child:
                self.set_direction("DOWN")

            self.ride_forward(self.distance_to_next_node(self.current_node, next_node), False)