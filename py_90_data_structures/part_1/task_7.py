# Найти длину окружности L и площадь круга S заданного радиуса R:
# L = 2·π·R, S = π·R^2, π=3.14

PI = 3.14


def get_circle_length(radius):
    circle_length = 2 * PI * radius
    return (round(circle_length, 2))


def get_circle_area(radius):
    circle_area = PI * pow(radius, 2)
    return (round(circle_area, 2))


r = float(input("Введите радиус: "))
print("Длина окружности:", get_circle_length(r))
print("Площадь круга:", get_circle_area(r))
