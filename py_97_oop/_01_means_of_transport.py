class MeansOfTransport:
    """Class for means of transport"""
    def __init__(self, *, brand: str, color: str) -> None:
        self._brand = brand
        self._color = color

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


class Car(MeansOfTransport):
    """Sublass for Cars"""

    car_drive = 4

    def __init__(self, *, brand: str, color: str, wheels_count: int, is_new: bool, models: list) -> None:
        super().__init__(brand=brand, color=color)
        self._wheels_count = wheels_count
        self.__is_new = is_new
        self._models = list(models)

    def __repr__(self):
        return self.__dict__

    def __str__(self):
        return f"{self.brand=}, {self.color=}, {self.wheels_count=}"

    def __getitem__(self, item):
        return self.models[item]

    def __eq__(self, item):
        if self.brand == item.brand:
            return f"This cars have the same brand: {self.brand}"
        else:
            return "Brands of this cars are different"

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    @property
    def wheels_count(self):
        return self._wheels_count

    @wheels_count.setter
    def wheels_count(self, wheels_count):
        self._wheels_count = wheels_count

    @property
    def models(self):
        return self._models

    @models.setter
    def models(self, models):
        self._models = models

    @classmethod
    def print_car_drive(cls) -> None:
        print(cls.car_drive)


class Moped(MeansOfTransport):
    """Sublass for Mopeds"""
    def __init__(self, *, brand: str, color: str, wheels_count: int) -> None:
        super().__init__(brand=brand, color=color)
        self._wheels_count = wheels_count

    @property
    def wheels_count(self):
        return self._wheels_count

    @wheels_count.setter
    def wheels_count(self, wheels_count):
        self._wheels_count = wheels_count

    @staticmethod
    def calculate_distance(*, time: int, max_speed: int) -> int:
        return time * max_speed


transport_1 = MeansOfTransport(brand="Toyota", color="Black")
print(transport_1.__dict__)
transport_1.brand = "Ford"
transport_1.color = "White"
print(transport_1.__dict__)

models_list = ["Polo", "Tiguan", "Jetta", "Passat"]
car_1 = Car(brand="Volkswagen", color="Silver", wheels_count=4, is_new=True, models=models_list)
print(car_1.__dict__)
moped_1 = Moped(brand="Subaru", color="Blue", wheels_count=2)
print(moped_1.__dict__)

calc_distance = Moped.calculate_distance(time=60, max_speed=201)
print(f"Moped travelled {calc_distance} meters")

# print(car_1._is_new)  # Outputs: True
# print(car_1.__is_new)  # Outputs: AttributeError: 'Car' object has no attribute '__is_new'
# print(car_1._Car__is_new)  # Outputs: True

Car.print_car_drive()

print(car_1.__repr__())  # reinitialized __repr__ method
print(car_1)  # reinitialized __str__ method
print(car_1[3])  # reinitialized __getitem__ method

car_2 = Car(brand="Volkswagen", color="Gray", wheels_count=4, is_new=False, models=models_list)

print(car_1.__eq__(car_2))  # reinitialized __eq__ method
car_1.new_attribute = "Honk"  # reinitialized __setattr__ method
car_2.models[2] = "Touareg"
print(car_1.__dict__)
print(car_2.__dict__)
