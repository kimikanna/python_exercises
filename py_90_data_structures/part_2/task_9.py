# Дано трёхзначное число. Используя одну операцию деления нацело,
# вывести первую цифру данного числа (сотни).

def get_first_digit(num):
    first_digit = num // 100
    return (first_digit)


num = int(input("Введите трёхзначное число: "))
f_digit = get_first_digit(num)
print("Первая цифра:", f_digit)
