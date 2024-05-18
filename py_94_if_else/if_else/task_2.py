# Даны два числа. Вывести большее из них.

def get_bigger_number(*args):
    if args[0] > args[1]:
        return args[0]
    else:
        return args[1]


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

result = get_bigger_number(first_number, second_number)
print(f"\nБольшее из чисел: {result}")
