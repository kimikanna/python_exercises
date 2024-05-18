"""
Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 — февраль и т. д.).
Определить количество дней в этом месяце для невисокосного года.
"""


def get_days_in_month(month):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return "31 день"
        case 4 | 6 | 9 | 11:
            return "30 дней"
        case 2:
            return "28 дней"
        case _:
            return 0


result = 0
while result == 0:
    month = int(input("Введите номер месяца (1-12): "))
    result = get_days_in_month(month)

print(f"В этом месяце {result}")
