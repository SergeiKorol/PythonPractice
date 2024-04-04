class LowFuelError(Exception):
    # Ошибка появится если топлива нет вовсе
    pass

class NotEnoughFuel(Exception):
    #Ошибка появится если топлива не достаточно
    pass

class CargoOverload(Exception):
    #Ошибка появляется если авто перегружено
    pass