"""
Дано целое число в диапазоне 100–999. Вывести строку-описание данного числа,
например: 256 — «двести пятьдесят шесть», 814 — «восемьсот четырнадцать».
"""


def num_to_text(number):
    if number < 100 or number > 999:
        return "Ошибка: некорректное число"

    first_digit = number // 100
    second_digit = number // 10 % 10
    third_digit = number % 10

    match first_digit:
        case 1:
            f_text = "Сто"
        case 2:
            f_text = "Двести"
        case 3:
            f_text = "Триста"
        case 4:
            f_text = "Четыреста"
        case 5:
            f_text = "Пятьсот"
        case 6:
            f_text = "Шестьсот"
        case 7:
            f_text = "Семьсот"
        case 8:
            f_text = "Восемьсот"
        case 9:
            f_text = "Девятьсот"
        case _:
            return "Ошибка: некорректное число"

    if second_digit == 1:
        match third_digit:
            case 0:
                s_text = " десять"
            case 1:
                s_text = " одиннадцать"
            case 2:
                s_text = " двенадцать"
            case 3:
                s_text = " тринадцать"
            case 4:
                s_text = " четырнадцать"
            case 5:
                s_text = " пятнадцать"
            case 6:
                s_text = " шестнадцать"
            case 7:
                s_text = " семнадцать"
            case 8:
                s_text = " восемнадцать"
            case 9:
                s_text = " девятнадцать"
            case _:
                return "Ошибка: некорректное число"
        return f_text + s_text

    match second_digit:
        case 0:
            s_text = ""
        case 2:
            s_text = " двадцать"
        case 3:
            s_text = " тридцать"
        case 4:
            s_text = " сорок"
        case 5:
            s_text = " пятьдесят"
        case 6:
            s_text = " шестьдесят"
        case 7:
            s_text = " семьдесят"
        case 8:
            s_text = " восемьдесят"
        case 9:
            s_text = " девяносто"
        case _:
            return "Ошибка: некорректное число"

    match third_digit:
        case 0:
            t_text = ""
        case 1:
            t_text = " один"
        case 2:
            t_text = " два"
        case 3:
            t_text = " три"
        case 4:
            t_text = " четыре"
        case 5:
            t_text = " пять"
        case 6:
            t_text = " шесть"
        case 7:
            t_text = " семь"
        case 8:
            t_text = " восемь"
        case 9:
            t_text = " девять"
        case _:
            return "Ошибка: некорректное число"

    return f_text + s_text + t_text


# n = int(input("Введите число (100-999): "))
for n in range(100, 1000):
    print(num_to_text(n))
