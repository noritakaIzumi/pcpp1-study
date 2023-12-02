class Tires:
    def __init__(self, size: int) -> None:
        self.__size = size

    def get_pressure(self):
        ...

    def pump(self):
        ...


class Engine:
    def __init__(self, fuel_type: str) -> None:
        self.__fuel_type = fuel_type

    def start(self):
        ...

    def stop(self):
        ...

    def get_state(self):
        ...


class Vehicle:
    # noinspection PyPep8Naming
    def __init__(self, VIN: str, engine: Engine, tires: Tires) -> None:
        self.__VIN = VIN
        self.__engine = engine
        self.__tires = tires


city_tires = Tires(15)
off_road_tires = Tires(18)
electric_engine = Engine('electric')
petrol_engine = Engine('petrol')
city_car = Vehicle('vin1', electric_engine, city_tires)
all_terrain_car = Vehicle('vin2', petrol_engine, off_road_tires)
