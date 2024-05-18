# Дано двузначное число. Вывести число, полученное при перестановке
# цифр исходного числа.

def reverse_number(num):
    first_digit = num // 10
    second_digit = num % 10
    reversed_num = second_digit * 10 + first_digit
    return (reversed_num)


num = int(input("Введите двузначное число: "))
r_num = reverse_number(num)
print("Число после перестановки:", r_num)
