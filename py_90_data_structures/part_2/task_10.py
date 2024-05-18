# Дано трехзначное число. Вывести вначале его последнюю цифру
# (единицы), а затем — его среднюю цифру (десятки).

def two_last_digits(num):
    third_digit = num % 10
    second_digit = num % 100 // 10
    return (third_digit, second_digit)


num = int(input("Введите трёхзначное число: "))
digits = two_last_digits(num)
print("Последняя цифра:", digits[0], "\nСредняя цифра:", digits[1])
