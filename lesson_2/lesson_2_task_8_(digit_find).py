# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

len = int(input('Сколько чисел вы собираетесь ввести? '))
digit = int(input('Какую цифру будем искать? '))
number = 0

for i in range(len):
    user_number = input('Число: ')
    count = user_number.count(str(digit))
    number += count

print(f'Цифра {digit} встретилась {number} раз')
