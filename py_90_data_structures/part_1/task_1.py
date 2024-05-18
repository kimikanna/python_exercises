# Дана сторона квадрата a. Найти его периметр P = 4·a

def get_perimeter(side):
    return(4 * side)


side = float(input("Введите длину стороны квадрата: "))
print("Периметр:", get_perimeter(side))