class MeansOfTransport():
    def __init__(self, brand: str, color: str) -> None:
        self.brand = brand
        self.color = color

    def show_brand(self) -> None:
        print(self.brand)

    def show_color(self) -> None:
        print(self.color)


car_1 = MeansOfTransport(brand="Toyota", color="Black")
car_1.show_brand()
car_1.show_color()
