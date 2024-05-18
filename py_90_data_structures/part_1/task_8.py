# Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2

def get_average(a, b):
    average = (a + b) / 2
    return (round(average, 2))


a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
print("Среднее арифметическое:", get_average(a, b))
