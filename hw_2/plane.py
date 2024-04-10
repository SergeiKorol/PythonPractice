from hw_2 import exceptions
from hw_2.base import Vehicle


class Plane(Vehicle):

    def __init__(self, weight: float = 100, fuel: float = 50, fuel_consumption: float = 10, max_cargo: float = 500):
        super().__init__()
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, amount: float) -> None:
        try:
            if self.cargo + amount <= self.max_cargo:
                self.cargo = (amount + self.cargo)
            else:
                raise exceptions.CargoOverload(amount, self.max_cargo)
        except exceptions.CargoOverload as ex:
            print(ex)

    def remove_all_cargo(self) -> float:
        cargo_before, self.cargo = self.cargo, 0
        return cargo_before

