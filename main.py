from time import sleep
from vehicle import Vehicle
from mapping_logic import MappingLogic

sleep(1)
print(1)
vehicle = Vehicle()
logic = MappingLogic(vehicle)
logic.run()
