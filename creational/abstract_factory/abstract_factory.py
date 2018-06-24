from creational.abstract_factory.factories import VehicleFactory, TrailerFactory


class FactoryProducer(object):

    @staticmethod
    def get_factory(choice):
        if choice:
            return {
                'vehicle': VehicleFactory(),
                'trailer': TrailerFactory(),
            }.get(choice.lower())

        return None
