from hw_2.base import Vehicle
from hw_2.engine import Engine

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.engine = None

    def set_engine(self, engine: Engine) -> None:
        self.engine = engine

