from creational.factory.vehicles import Car, Lorry, Van


class VehicleFactory(object):

    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type:
            return {
                'car': Car(),
                'lorry': Lorry(),
                'van': Van(),
            }.get(vehicle_type.lower())

        return None
