class LowFuelError(Exception):
    # Ошибка появится если топлива нет вовсе
    pass

class NotEnoughFuel(Exception):
    # Ошибка появится если топлива не достаточно
    def __int__(self, fuel, required_fuel):
        self.fuel = fuel
        self.required_fuel = required_fuel
    def __str__(self):
            return print(f"Требутся дополнительно: {self.fuel - self.required_fuel}")

class CargoOverload(Exception):
    #Ошибка появляется если авто перегружено
    pass
