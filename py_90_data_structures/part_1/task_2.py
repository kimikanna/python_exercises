# Дана сторона квадрата a. Найти его площадь {{S = a^2}}

def get_area(side):
    return(pow(side, 2))


side = float(input("Введите длину стороны квадрата: "))
print("Площадь:", get_area(side))