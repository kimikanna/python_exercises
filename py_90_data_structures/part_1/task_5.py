# Дана длина ребра куба a. Найти объем куба V = a^3
# и площадь его поверхности S = 6·a^2

def get_volume(side):
    volume = pow(side, 3)
    return(round(volume), 2)

def get_surface_area(side):
    surface_area = 6 * pow(side, 2)
    return(round(surface_area), 2)


side = float(input("Введите длину ребра куба: "))
print("\nОбъём:", get_volume(side))
print("Площадь поверхности:", get_surface_area(side))