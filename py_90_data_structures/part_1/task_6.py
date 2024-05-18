# Даны длины ребер a, b, c прямоугольного параллелепипеда.
# Найти его объем V = a·b·c и площадь поверхности
# S = 2·(a·b + b·c + a·c)

def get_volume(side_a, side_b, side_c):
    volume = side_a * side_b * side_c
    return (round(volume, 2))


def get_surface_area(side_a, side_b, side_c):
    surface_area = 2 * (side_a * side_b + side_b * side_c + side_a * side_c)
    return (round(surface_area, 2))


a = float(input("Введите длину прямоугольного параллелепипеда: "))
b = float(input("Введите его ширину: "))
c = float(input("Введите его высоту: "))

print("\nОбъём:", get_volume(a, b, c))
print("Площадь поверхности:", get_surface_area(a, b, c))
