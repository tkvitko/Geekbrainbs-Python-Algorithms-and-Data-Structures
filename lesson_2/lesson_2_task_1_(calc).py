# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

operation = None

while operation != 0:
    number1 = float(input('Введите первое число: '))
    number2 = float(input('Введите второе число: '))
    operation = input('Введите знак операции: ')
    if operation == '+':
        print(f'{number1 + number2}')
    elif operation == '-':
        print(f'{number1 - number2}')
    elif operation == '*':
        print(f'{number1 * number2}')
    elif operation == '/':
        if number2 == 0:
            print('Не надо так')
        else:
            print(f'{number1 / number2}')
    elif operation == '0':
        operation = int(operation)
    else:
        print('Вы ввели что-то не то')
