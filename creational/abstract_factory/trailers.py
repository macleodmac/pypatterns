
class Trailer(object):
    VOLUME = 250  # litres

    def __init__(self, volume_filled=0):
        self.volume_filled = volume_filled

    def fill(self, litres):
        self.volume_filled += litres

    def remove(self, litres):
        self.volume_filled -= litres

    def get_fill_level(self):
        return self.volume_filled

    def get_max_volume(self):
        return self.VOLUME


class BikeTrailer(Trailer):
    VOLUME = 200


class LongTrailer(Trailer):
    VOLUME = 500


class ExtraLongTrailer(Trailer):
    VOLUME = 1000
