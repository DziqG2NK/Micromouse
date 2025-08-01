from vehicle import Vehicle
from virtual_sensor import vSensor
from directions import Direction
from map import Map
from mapping_logic import MappingLogic
from path_finder import PathFinder

# loading map

def all_measurements(vehicle):
    dirs = [Direction.LEFT, Direction.UP, Direction.RIGHT]
    for dir in dirs:
        print(f"{dir}: {vehicle.measure_distance(dir)}")

def create_virtual_vehicle():
    sensor_l = vSensor(Direction.LEFT, map)
    sensor_u = vSensor(Direction.UP, map)
    sensor_r = vSensor(Direction.RIGHT, map)

    vehicle = Vehicle(sensor_l, sensor_u, sensor_r)
    vehicle.set_pos(*map.get_start())
    vehicle.you_are_in_the_Matrix_Neo()

    sensor_l.load_vehicle(vehicle)
    sensor_u.load_vehicle(vehicle)
    sensor_r.load_vehicle(vehicle)

    return vehicle

map = Map(r'C:\Users\Domin\Documents\GitHub\Micromouse\simulation\backtracking_map.png')

car = create_virtual_vehicle()

map.add_vehicle(car)
car.dir = Direction.DOWN

engine = MappingLogic(car)
engine.run()
start = engine.start
sp = PathFinder(car, start)
print(sp.find_path_to_finish())


# map.display_map()

# current_node = engine.start
#
# while current_node is not None:
#     map.display_map()
#     all_measurements(car)
#     current_node = engine.run_cycle(current_node)

# print(car.get_pos())
#
# engine.backtrack(last_node)
# map.display_map()
# print(car.get_pos())


