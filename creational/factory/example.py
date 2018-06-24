from creational.factory import factory_classic
from creational.factory import factory_pythonic


car = factory_classic.VehicleFactory.get_vehicle('car')
print("Car max speed: {}".format(car.get_max_speed()))

van = factory_classic.VehicleFactory.get_vehicle('van')
print("Van max speed: {}".format(van.get_max_speed()))

lorry = factory_pythonic.get_vehicle('lorry')
print("Lorry max speed: {}".format(lorry.get_max_speed()))

