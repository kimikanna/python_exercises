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


car_1 = MeansOfTransport(brand="Toyota", color="Black")
print(car_1.__dict__)
car_1.brand = "Ford"
car_1.color = "White"
print(car_1.__dict__)
