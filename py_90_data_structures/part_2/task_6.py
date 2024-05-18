# Дано двузначное число. Вывести вначале его левую цифру (десятки),
# а затем — его правую цифру (единицы).

def split_two_digit(num):
    first_digit = num // 10
    second_digit = num % 10
    return (first_digit, second_digit)


num = int(input("Введите двузначное число: "))
tpl = split_two_digit(num)
print("Десятки:", tpl[0], "\nЕдиницы:", tpl[1])
