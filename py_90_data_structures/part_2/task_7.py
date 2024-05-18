# Дано двузначное число. Найти сумму и произведение его цифр.

def get_sum_and_product(num):
    first_digit = num // 10
    second_digit = num % 10
    sum = first_digit + second_digit
    product = first_digit * second_digit
    return (sum, product)


num = int(input("Введите двузначное число: "))
tpl = get_sum_and_product(num)
print("Сумма цифр:", tpl[0], "\nПроизведение цифр:", tpl[1])
