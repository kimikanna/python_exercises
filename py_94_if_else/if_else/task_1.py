# Даны три целых числа. Найти количество положительных чисел в исходном наборе.

def count_positive(*args):
    count = 0
    for arg in args:
        if arg > 0:
            count += 1

    return count


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число: "))

result = count_positive(first_number, second_number, third_number)
print(f"Количество положительных чисел: {result}")
