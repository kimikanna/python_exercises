"""
*** Реализуйте программу калькулятор. На вход подается три значения:
первое число, второе число и операция(*, /, + или -).
На выходе должны получить число, после выполнения операции.
"""

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
operator = input("Введите операцию (*, /, + или -): ")

match operator:
    case "*":
        result = a * b
    case "/":
        if b == 0:
            raise ZeroDivisionError("Ошибка: деление на ноль")
        else:
            result = round(a / b, 2)
    case "+":
        result = a + b
    case "-":
        result = a - b
    case "^":
        result = a ** b
    case _:
        result = "Ошибка: некорректный оператор"

print(f"Результат вычисления: {result}")
