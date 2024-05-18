# Даны два числа. Вывести вначале большее, а затем меньшее из них.

def get_bigger_number(first_num, second_num):
    if first_num > second_num:
        return first_num, second_num
    else:
        return second_num, first_num


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

result = get_bigger_number(first_number, second_number)
print(f"\nБольшее из чисел: {result[0]}")
print(f"Меньшее из чисел: {result[1]}")
