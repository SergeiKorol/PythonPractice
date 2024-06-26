from abc import ABC

from hw_2 import exceptions


class Vehicle(ABC):
 
    def __init__(self, weight: float =100, fuel: float =50, fuel_consumption: float =10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self)-> None:
        try:
            if not self.started:
                if self.fuel > 0:
                    self.started = True
                else:
                    raise exceptions.LowFuelError()

        except exceptions.LowFuelError as ex:
            print(ex)

    def move(self, distance: float)-> None:
        try:
            if self.started:
                required_fuel = distance / self.fuel_consumption
                if required_fuel <= self.fuel:
                    self.fuel = self.fuel - required_fuel
                else:
                    raise exceptions.NotEnoughFuel(self.fuel, required_fuel)
        except exceptions.NotEnoughFuel as ex:
            print(ex)



