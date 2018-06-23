from creational.factory.vehicles import Car, Lorry, Van


class VehicleFactory(object):

    @staticmethod
    def get_vehicle(vehicle_type):

        if not vehicle_type:
            return None

        if vehicle_type.lower() == 'car':
            return Car()
        elif vehicle_type.lower() == 'lorry':
            return Lorry()
        elif vehicle_type.lower() == 'van':
            return Van()

        return None
