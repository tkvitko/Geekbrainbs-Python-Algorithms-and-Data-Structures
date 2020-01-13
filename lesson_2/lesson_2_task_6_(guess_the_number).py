# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.

import random

number = random.randint(0, 100)
tries = 10
user_number = None

while user_number != number and tries != 0:
    user_number = int(input('Введите число: '))
    tries -= 1
    if user_number > number:
        print('Слишком много')
    elif user_number < number:
        print('Слишком мало')
else:
    print(f'Игра окончена, правильный ответ: {number}')