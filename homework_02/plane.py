from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload
"""
создайте класс `Plane`, наследник `Vehicle`
"""


class Plane(Vehicle):

    cargo = 0

    def __init__(self, weight=100, fuel=20, fuel_consumption=0.05, max_cargo=200):
        super(Plane, self).__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, add_cargo):
        if self.cargo + add_cargo > self.max_cargo:
            raise CargoOverload('Cargo overload!')
        else:
            self.cargo += add_cargo

    def remove_all_cargo(self):
        cargo_before_remove = self.cargo
        self.cargo = 0
        return cargo_before_remove



