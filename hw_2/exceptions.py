class LowFuelError(Exception):
    # Ошибка появится если топлива нет вовсе
    def __str__(self):
        return f"Просто добавь бензин:"


class NotEnoughFuel(Exception):
    # Ошибка появится если топлива не достаточно
    def __init__(self, fuel, required_fuel):
        self.fuel = fuel
        self.required_fuel = required_fuel

    def __str__(self):
        return f"Требутся дополнительно: {self.fuel - self.required_fuel}"


class CargoOverload(Exception):
    # Ошибка появляется если авто перегружено
    def __init__(self, amount, max_cargo):
        self.amount = amount
        self.max_cargo = max_cargo

    def __str__(self):
        return f"Перегруз на: {self.max_cargo - self.amount}"
