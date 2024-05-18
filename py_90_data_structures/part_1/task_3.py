# Даны стороны прямоугольника a и b. Найти его площадь S = a·b
# и периметр P = 2·(a + b)

def get_area(side_a, side_b):
    return(side_a * side_b)

def get_perimeter(side_a, side_b):
    return(2 * (side_a + side_b))


side_a = float(input("Введите длину прямоугольника: "))
side_b = float(input("Введите ширину прямоугольника: "))
print("\nПлощадь:", get_area(side_a, side_b))
print("Периметр:", get_perimeter(side_a, side_b))