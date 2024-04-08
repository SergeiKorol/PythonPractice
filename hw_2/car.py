from hw_2.base import Vehicle
from hw_2.engine import Engine

class Car(Vehicle):

    def set_engine(self, engine: Engine) -> None:
        self.engine = engine
