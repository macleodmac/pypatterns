

class VehicleFactory(object):

    @staticmethod
    def get_vehicle(vehicle_type):

        if not vehicle_type:
            return None