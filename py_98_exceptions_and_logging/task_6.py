"""
Написать программу для генерации случайных чисел в заданном диапазоне.
Если пользователь ввёл недопустимые границы диапазона (например, меньше нуля),
программа должна вывести ошибку и попросить ввести диапазон заново.
ИНформация об ошибках должна быть записана в лог.
"""

import random
import logging


def get_random_generator(left_bound, right_bound):
    if left_bound < 0 or right_bound < 0:
        raise ValueError(
            "Недопустимый диапазон: значение одной из границ меньше нуля")
    if left_bound > right_bound:
        raise ValueError("Недопустимый диапазон: левая граница больше правой")

    def random_generator(left_bound, right_bound):
        while True:
            yield random.randint(left_bound, right_bound)
    return random_generator(left_bound, right_bound)


def main():
    logging.basicConfig(filename="task_6_log.log",
                        encoding="utf-8",
                        level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s",
                        datefmt="%Y:%m:%d %H:%M:%S")
    while True:
        try:
            left_bound = int(input("Введите левую границу диапазона: "))
            right_bound = int(input("Введите правую границу диапазона: "))
            random_generator = get_random_generator(left_bound, right_bound)
            break
        except ValueError as e:
            logging.error(e)
            print(e)
    logging.info(f"Генератор успешно создан")
    for _ in range(10):
        print(next(random_generator))


if __name__ == "__main__":
    main()
