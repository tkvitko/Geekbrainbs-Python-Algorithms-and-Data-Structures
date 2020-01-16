# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

# целые числа
min_int = int(input('Введите начало диапазона (целые): '))
max_int = int(input('Введите конец диапазона (целые): '))
# По-хорошему здесь тоже сделать проверку, что max > min
random_int = random.randint(min_int, max_int)
print(f'Случайное целое: {random_int}')

min_float = float(input('Введите начало диапазона (вещественные): '))
max_float = float(input('Введите конец диапазона (вещественные): '))

random_float = random.uniform(min_float, max_float)
print(f'Случайное вещественное: {random_float}')

# буквы
alphabet = 'abcdefghijklmnopqrstuywxyz'

min_letter = input('Введите начало диапазона (буквы): ')
max_letter = input('Введите конец диапазона (буквы): ')
min_letter_number = alphabet.index(min_letter)
max_letter_number = alphabet.index(max_letter)

# Защитимся от того, что пользователь ввел буквы не в порядке алфавита
if max_letter_number < min_letter_number:
    temp = max_letter_number
    max_letter_number = min_letter_number
    min_letter_number = temp
else:
    pass

random_letter_number = random.randint(min_letter_number, max_letter_number)
random_letter = alphabet[random_letter_number]
print(f'Случайная буква: {random_letter}')
