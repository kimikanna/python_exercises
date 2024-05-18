"""
Робот может перемещаться в четырех направлениях («С» — север, «З» — запад,
«Ю» — юг, «В» — восток) и принимать три цифровые команды: 0 — продолжать
движение, 1 — поворот налево, −1 — поворот направо. Дан символ C — исходное
направление робота и целое число N — посланная ему команда.
Вывести направление робота после выполнения полученной команды.
"""


def get_direction(c, n):
    directions = {"С": "З", "З": "Ю", "Ю": "В", "В": "С"}
    if c not in directions.keys():
        return "О"

    match n:
        case 0:
            return c
        case 1:
            return directions[c]
        case -1:
            for key, val in directions.items():
                if val == c:
                    return key
            else:
                return "О"
        case _:
            return "О"


c = input("Введите направление: ")
n = int(input("Введите команду: "))

result = get_direction(c, n)
dir_fullnames = {"С": "Север", "З": "Запад",
                 "Ю": "Юг", "В": "Восток", "О": "Ошибка"}
print(f"\nНовое направление: {dir_fullnames[result]}")
