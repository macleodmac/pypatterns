from creational.abstract_factory.trailers import BikeTrailer, LongTrailer, ExtraLongTrailer
from creational.abstract_factory.vehicles import Car, Lorry, Van


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


class TrailerFactory(object):

    @staticmethod
    def get_trailer(trailer_type):
        if trailer_type:
            return {
                'bike': BikeTrailer(),
                'long': LongTrailer(),
                'extralong': ExtraLongTrailer(),
            }.get(trailer_type.lower())

        return None
