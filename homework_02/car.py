from homework_02.base import Vehicle
from homework_02.engine import Engine
"""
создайте класс `Car`, наследник `Vehicle`
"""


class Car(Vehicle):

    engine: Engine

    def __init__(self, weight=100, fuel=20, fuel_consumption=0.05):
        super(Car, self).__init__(weight, fuel, fuel_consumption)

    def start(self):
        super(Car, self).start()

    def move(self, distance):
        super(Car, self).move(distance)

    def set_engine(self, engine):
        self.engine = engine



