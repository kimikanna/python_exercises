"""
Даны координаты точки, не лежащей на координатных осях OX и OY.
Определить номер координатной четверти, в которой находится данная точка.
Координаты задаются пользователем, например (10, 15).
"""


def get_quarter(x, y):
    if x == 0 or y == 0:
        raise ValueError(
            "\nТочка находится на координатной оси. Введите ненулевые значения")

    temp = x * y
    if temp > 0:
        if x > 0:
            return "I"
        else:
            return "III"

    else:
        if x < 0:
            return "II"
        else:
            return "IV"


x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))

try:
    result = get_quarter(x, y)
except ValueError as e:
    print(e)
else:
    print(f"\nТочка находится в {result} четверти")
