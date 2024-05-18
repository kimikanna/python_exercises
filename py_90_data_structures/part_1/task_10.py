# Даны два ненулевых числа. Найти сумму, разность, произведение
# и частное их квадратов.

def get_sqare(num):
    sqared = num ** 2
    return (sqared)


def rounded_print(string, c):
    print(string, round(c, 2))


a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

rounded_print("Сумма квадратов:", get_sqare(a) + get_sqare(b))
rounded_print("Разность квадратов:", get_sqare(a) - get_sqare(b))
rounded_print("Произведение квадратов:", get_sqare(a) * get_sqare(b))
rounded_print("Частное квадратов:", get_sqare(a) / get_sqare(b))
