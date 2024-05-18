"""
Напишите программу для подсчета среднего числа всех введенных пользователям чисел.
Ввод пользователя должен осуществляться с помощью input. Если пользователь вводит ноль,
то выводиться на экран среднее значение. Используйте цикл while для решения данной задачи
"""


def calculate_average():
    numbers = []
    while True:
        number = int(input("Введите число (0 для выхода): "))
        if number == 0:
            break
        numbers.append(number)

    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"Среднее значение: {average}")
    else:
        print("Вы не ввели ни одного числа.")


calculate_average()
