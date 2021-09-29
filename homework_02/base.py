from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False

    # стандартный расход 0.05 единиц топлива на 1 единицу дистанции
    def __init__(self, weight=100, fuel=20, fuel_consumption=0.05):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('Low fuel error')

    def move(self, distance):
        consumption = self.fuel_consumption * distance
        if self.fuel < consumption:
            raise NotEnoughFuel('Not enough fuel')
        else:
            self.fuel -= consumption





