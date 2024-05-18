"""
Даны два целых числа: D (день) и M (месяц), определяющие правильную дату
невисокосного года. Вывести значения D и M для даты, следующей за указанной.
"""


def get_days_in_month(day, month):
    match day, month:
        case 31, 1 | 3 | 5 | 7 | 8 | 10:
            return 1, month + 1
        case 30, 4 | 6 | 9 | 11:
            return 1, month + 1
        case 28, 2:
            return 1, 3
        case 31, 12:
            return 1, 1
        case _:
            return day + 1, month


d = int(input("Введите день (1-31): "))
m = int(input("Введите месяц (1-12): "))

result = get_days_in_month(d, m)
print(f"\nЗавтра {result[0]}-{result[1]}")
