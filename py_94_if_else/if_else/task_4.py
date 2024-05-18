# Даны три числа. Найти наименьшее из них.

def get_smaller_number(*args):
    if args[0] < args[1]:
        if args[0] < args[2]:
            return args[0]
    if args[1] < args[2]:
        return args[1]
    else:
        return args[2]


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число: "))

result = get_smaller_number(first_number, second_number, third_number)
print(f"\nМеньшее из чисел: {result}")
