# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

# Функция для подсчета суммы цифр натурального числа
def digits_sum(number):
    sum = 0
    while number > 0:
        digit = number % 10
        number //= 10
        sum = sum + digit
    return sum


# Позволим пользователю выбрать, сколько чисел он собирается вводить
count = int(input('Сколько чисел вы собираетесь ввести? '))
max = 0

for i in range(count):
    user_number = int(input('Число: '))
    this_sum = digits_sum(user_number)
    if this_sum > max:
        max = this_sum
        result_number = user_number

print(f'Число-победитель: {result_number}')
print(f'Сумма его цифр: {max}')
