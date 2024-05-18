# Даны два неотрицательных числа a и b. Найти их среднее
# геометрическое, т. е. квадратный корень из их произведения: sqrt(a·b)

def get_geometric_mean(a, b):
    geometric_mean = pow(a * b, 0.5)
    return (round(geometric_mean, 2))


a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
print("Среднее геометрическое:", get_geometric_mean(a, b))
