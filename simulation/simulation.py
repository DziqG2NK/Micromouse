from vehicle import Vehicle
from virtual_sensor import vSensor
from directions import Direction
from map import Map
from mapping_logic import MappingLogic

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

map = Map(r'C:\Users\Domin\Documents\GitHub\Micromouse\simulation\spiral_map.png')

car = create_virtual_vehicle()

map.add_vehicle(car)

engine = MappingLogic(car)
engine.run()

map.display_map()


all_measurements(car)
print("TEST")

