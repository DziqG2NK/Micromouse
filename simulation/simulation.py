from vehicle import Vehicle
from virtual_sensor import vSensor
from directions import Direction
from map import Map

# loading map

def all_measurements():
    for dir in dirs:
        print(f"{dir}: {car.measure_distance(dir)}")


map = Map(r'C:\Users\Domin\Documents\GitHub\Micromouse\simulation\example_map.png')

map.display_map()

dirs = [Direction.LEFT, Direction.UP, Direction.RIGHT]

sensor_l = vSensor(Direction.LEFT, map)
sensor_u = vSensor(Direction.UP, map)
sensor_r = vSensor(Direction.RIGHT, map)

car = Vehicle(sensor_l, sensor_u, sensor_r)
car.set_pos(*map.get_start())
car.you_are_in_the_Matrix_Neo()

sensor_l.load_vehicle(car)
sensor_u.load_vehicle(car)
sensor_r.load_vehicle(car)

all_measurements()

car.set_direction(Direction.RIGHT)

all_measurements()

car.ride_forward(30)
all_measurements()