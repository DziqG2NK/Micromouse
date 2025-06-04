from directions import Direction


class vSensor:
    def __init__(self, direction, map=None, vehicle=None):
        self.direction = direction
        self.map = map
        self.vehicle = vehicle

    def load_map(self, map):
        self.map = map

    def load_vehicle(self, vehicle):
        self.vehicle = vehicle

    def measure(self):
        veh_dir = self.vehicle.dir.value
        veh_pos = [self.vehicle.x, self.vehicle.y]
        measure_dir = Direction((self.direction.value + veh_dir) % 4)

        wall_pos = veh_pos.copy()

        if measure_dir == Direction.UP:
            while self.map.grid[wall_pos[0]][wall_pos[1]] == 0:
                wall_pos[1] -= 1
            return abs(wall_pos[1] - veh_pos[1])
        elif measure_dir == Direction.RIGHT:
            while self.map.grid[wall_pos[0]][wall_pos[1]] == 0:
                wall_pos[0] += 1
            return abs(wall_pos[0] - veh_pos[0])
        elif measure_dir == Direction.LEFT:
            while self.map.grid[wall_pos[0]][wall_pos[1]] == 0:
                wall_pos[0] -= 1
            return abs(veh_pos[0] - wall_pos[0])
        elif measure_dir == Direction.DOWN:
            while self.map.grid[wall_pos[0]][wall_pos[1]] == 0:
                wall_pos[1] += 1
            return abs(veh_pos[1] - wall_pos[1])

