
class Vehicle(object):

    MAX_SPEED = 500

    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self, speed):
        new_speed = self.speed + speed
        self.speed = min(new_speed, self.MAX_SPEED)

    def decelerate(self, speed):
        new_speed = self.speed - speed
        self.speed = max(new_speed, 0)

    def get_max_speed(self):
        return self.MAX_SPEED


class Car(Vehicle):
    MAX_SPEED = 155


class Van(Vehicle):
    MAX_SPEED = 90


class Lorry(Vehicle):
    MAX_SPEED = 70
