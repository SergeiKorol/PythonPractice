from abc import ABC

from hw_2 import exceptions


class Vehicle(ABC):
    weight: float
    fuel: float
    fuel_consumption: float
    started: bool

    def __init__(self, weight: float =100, fuel: float =50, fuel_consumption: float =10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self)-> None:
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError("Not enough fuel to start the vehicle")

    def move(self, distance: float)-> None:
        if self.started:
            required_fuel = distance / self.fuel_consumption
            if required_fuel <= self.fuel:
                self.fuel = self.fuel - required_fuel
            else:
                raise exceptions.NotEnoughFuel("Not enough fuel to cover the distance")

