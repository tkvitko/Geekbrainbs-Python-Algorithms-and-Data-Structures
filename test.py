"""
Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

count_digit = int(input("Сколько чисел будет введено:\n>>>"))
count = 0
digit = None
max = 0
rez = None
for i in range(count_digit):
    user_input = abs(int(input(f"Введите {i + 1} чмсло\n>>>")))
    digit = user_input
    while user_input != 0:
        count += user_input % 10
        user_input //= 10
    if max < count:
        max = count
        rez = digit
    count = 0

if rez:
    print(f"Число - {rez} с максимальной суммой цифр {max}")
else:
    print("Некорректный ввод")


