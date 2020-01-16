# 4. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

alphabet = 'abcdefghijklmnopqrstuywxyz'

letter_1 = input('Введите первую букву: ')
letter_2 = input('Введите вторую букву: ')
letter_1_number = alphabet.index(letter_1) + 1
letter_2_number = alphabet.index(letter_2) + 1

if letter_1_number == letter_2_number:
    range = 0
else:
    range = abs(letter_2_number - letter_1_number) - 1

print(f'Позиция первой буквы: {letter_1_number}')
print(f'Позиция второй буквы: {letter_2_number}')
print(f'Между ними {range} символа')
