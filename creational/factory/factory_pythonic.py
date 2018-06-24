from creational.factory.vehicles import Car, Lorry, Van


def get_vehicle(vehicle_type):
    if vehicle_type:
        return {
            'car': Car(),
            'lorry': Lorry(),
            'van': Van(),
        }.get(vehicle_type.lower())

    return None
