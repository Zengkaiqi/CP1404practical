from prac_09.car import Car
from random import randint
class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self,distance):
        random_number = randint(0,100)
        if random_number < self.reliability:
            super().drive(random_number)
        else:
            print("it is not reliable")


