from hw_2.base import Vehicle
from hw_2.engine import Engine

class Car(Vehicle):
    def __init__(self, weight: float = 100, fuel: float = 50, fuel_consumption: float = 10):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine: Engine) -> None:
        self.engine = engine

