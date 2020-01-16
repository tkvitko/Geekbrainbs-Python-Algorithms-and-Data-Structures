# 5. Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.

alphabet = 'abcdefghijklmnopqrstuywxyz'

number = int(input('Введите номер буквы (от 1 до 26): '))
letter = alphabet[number - 1]
print(f'С этим номером буква: {letter}')
