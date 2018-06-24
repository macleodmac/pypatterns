from creational.abstract_factory.abstract_factory import FactoryProducer


vehicle_factory = FactoryProducer.get_factory('vehicle')
car = vehicle_factory.get_vehicle('car')
print("Car max speed: {}".format(car.get_max_speed()))

van = vehicle_factory.get_vehicle('van')
print("Van max speed: {}".format(van.get_max_speed()))


trailer_factory = FactoryProducer.get_factory('trailer')
extra_long = trailer_factory.get_trailer('extralong')
print("Extra Long trailer max volume: {}".format(extra_long.get_max_volume()))

bike = trailer_factory.get_trailer('bike')
print("Bike trailer max volume: {}".format(bike.get_max_volume()))
