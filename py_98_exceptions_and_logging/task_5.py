"""
Написать программу на Python для решения квадратного уравнения ax^2 + bx + c = 0. 
Если дискриминант отрицателен, программа должна выдать ошибку
и предложить пользователю попробовать еще раз с другими коэффициентами.
При выполнении скрипта в лог должна записываться информация об успехе или неудаче операции.
"""
import logging


class DiscriminantError(Exception):
    """Исключение, вызываемое при отрицательном значении дискриминанта"""

    def __init__(self, message):
        super().__init__(message)


def get_discriminant(a, b, c):
    return b**2 - 4 * a * c


def solve_equation(a, b, c, accuracy):
    discriminant = get_discriminant(a, b, c)
    if discriminant < 0:
        raise DiscriminantError("Отрицательный дискриминант")
    x1 = (-b + discriminant**0.5) / (2 * a)
    x2 = (-b - discriminant**0.5) / (2 * a)
    return round(x1, accuracy), round(x2, accuracy)


def main():
    logging.basicConfig(filename="task_5_log.log",
                        encoding="utf-8",
                        level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format="%(asctime)s [%(levelname)s] %(message)s")

    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    c = int(input("Введите c: "))

    try:
        x1, x2 = solve_equation(a, b, c, 2)
        b_sign = "+" if b > 0 else "-"
        c_sign = "+" if c > 0 else "-"
        print(f"Уравнение: {a}x^2 {b_sign} {abs(b)}x {c_sign} {abs(c)}")
        print(f"Корни уравнения: {x1}, {x2}")
    except DiscriminantError as e:
        print("Произошла ошибка:", e)
        logging.error("Произошла ошибка при решении уравнения!")
    else:
        logging.info("Уравнение решено успешно!")


if __name__ == "__main__":
    main()
