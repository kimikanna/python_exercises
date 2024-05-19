# Реализуйте абстрактный класс Animals, создайте класс Cat, котрый будет наследоваться от класса Animals
# и реализуйте метод voice. Реализуйте класс Dog. Придумайте, какие переменные будет принимать данный класс
# и какие методы будут реализованы. Реализуйте в этом классе паттерн Singleton

class Animals:

    def __init__(self, age: int, color: str, paws_count: int = 4) -> None:
        self.age = age
        self.color = color
        self.paws_count = paws_count


class Cat(Animals):
    @staticmethod
    def voice() -> str:
        return "Meow"

    def info(self) -> str:
        return f"Cat's age is: {self.age}, color: {self.color}"


class Dog(Animals):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, age, color, name, paws_count=4) -> None:
        super().__init__(age, color, paws_count)
        self.name = name

    def info(self) -> str:
        return f"Dog's name is: {self.name}, age: {self.age}, color: {self.color}"


my_cat = Cat(3, "Gray")
print(f"Cat's voice is: {my_cat.voice()}")
print(my_cat.info())

print("-----------")

dog_1 = Dog(5, "Black", "Bim")
print(dog_1.info())
dog_2 = Dog(3, "Ginger", "Dark")
print(dog_2.info())
print(dog_1.info())  # Outputs dog_2 data, because of singleton
