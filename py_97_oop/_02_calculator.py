# Реализуйте класс Calculator, в котором будет один метод, для вычисления суммы двух чисел.
# Реализуйте еще один класс, который будет наследоваться от класса Calculator и перегрузите метод
# для вычисления суммы двух чисел, чтобы он делал конкатенацию двух строк.

class Calculator:
    """Класс Calculator, вычисляющий сумму двух чисел"""

    @staticmethod
    def addition(*, operand_a: int | float, operand_b: int | float) -> float:
        return operand_a + operand_b


class Concatenation(Calculator):
    """Класс Concatenation, возвращающий результат конкатенации двух чисел"""

    @staticmethod
    def addition(*, operand_a: int | float | str, operand_b: int | float | str) -> str:
        return str(operand_a) + str(operand_b)


print(Calculator.addition(operand_a=2, operand_b=3.5))  # Outputs: 5.5
print(Concatenation.addition(operand_a=2, operand_b=3.5))  # Outputs: 23.5
