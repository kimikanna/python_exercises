# Реализуйте абстрактный класс Animals, создайте класс Cat, котрый будет наследоваться от класса Animals
# и реализуйте метод voice. Реализуйте класс Dog. Придумайте, какие переменные будет принимать данный класс
# и какие методы будут реализованы. Реализуйте в этом классе паттерн Singleton

from abc import ABCMeta, abstractmethod


class Animals:
    """Abstract class for Animals"""

    __metaclass__ = ABCMeta

    def __init__(self, age: int, color: str, voice_tone: str, paws_count: int = 4) -> None:
        self.age = age
        self.color = color
        self.voice_tone = voice_tone
        self.paws_count = paws_count

    @abstractmethod
    def voice(self):
        """Узнать голос"""


class Cat(Animals):
    """Class for Cats"""

    def __init__(self, age: int, color: str, voice_tone: str, paws_count: int = 4) -> None:
        super().__init__(age, color, voice_tone, paws_count)

    def voice(self) -> str:
        return f"Cat's voice is: {self.voice_tone}"

    def info(self) -> str:
        return f"Cat's age is: {self.age}, color: {self.color}"


class Dog(Animals):
    """Class for Dogs, using singleton"""

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, age: int, color: str, voice_tone: str, name: str, paws_count: int = 4) -> None:
        super().__init__(age, color, voice_tone, paws_count)
        self.name = name

    def voice(self) -> str:
        return f"Dog's voice is: {self.voice_tone}"

    def info(self) -> str:
        return f"Dog's name is: {self.name}, age: {self.age}, color: {self.color}"


my_cat = Cat(3, "Gray", "Meow")
print(f"Cat's voice is: {my_cat.voice()}")
print(my_cat.info())

print("-----------")

dog_1 = Dog(5, "Black", "Bark", "Bim")
print(dog_1.info())
print(dog_1.voice())
dog_2 = Dog(3, "Ginger", "Howl", "Dark")
print(dog_2.info())
print(dog_1.info())  # Outputs dog_2 data, because of singleton
print(dog_1.voice())  # Outputs "Howl", because of singleton
